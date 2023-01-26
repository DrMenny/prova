from pprint import pprint

import requests

all_objs = requests.get('http://44.234.191.4:8194/ds4biz/predictor/0.0/predictors',
                        params={'info':'true'})

pprint(all_objs.json())

sticazzi = requests.post('http://44.234.191.4:8194/ds4biz/predictor/0.0/predictors/mimmo',
              params={'description':'ciao',
                      'model_id':'auto',
                      'transformer_id':'auto'})

print(sticazzi.text)

url = 'http://44.234.191.4:8194/ds4biz/predictor/0.0/predictors/mimmo/fit'

body = {"data": [{"text": "Lorem ipsum dolor sit amet, consectetur. c1"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c1"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c2"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c2"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c3"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c3"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c4"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c4"}],
        "target": ["a", "a", "a", "a", "b", "b", "b", "b"]}

sticazzi = requests.post(url, json=body, params={'report':'true'})

print(sticazzi.text)
