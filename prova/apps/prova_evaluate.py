from pprint import pprint

import requests

url = 'http://44.234.191.4:8194/ds4biz/predictor/0.0/predictors/mimmo/evaluate'

body = {"data": [{"text": "Lorem ipsum dolor sit amet, consectetur. c1"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c1"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c2"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c2"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c3"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c3"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c4"},
                {"text": "Lorem ipsum dolor sit amet, consectetur. c4"}],
        "target": ["a", "a", "a", "a", "b", "b", "b", "b"]}

parameters = {'branch':'development'}

eva = requests.post(url, json=body, params=parameters)

pprint(eva.json())