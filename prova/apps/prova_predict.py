import requests

url = 'http://44.234.191.4:8194/ds4biz/predictor/0.0/predictors/mimmo/predict'

body = [{"text": "Lorem ipsum dolor sit amet, consectetur. c1"}]

parameters = {'branch':'development'}

pred = requests.post(url, json=body, params=parameters)

print(pred.json())