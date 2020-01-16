import yaml
import requests

with open('milk.yaml', 'r') as f:
    data = yaml.load(f.read())

password = 'test_password'

url = 'https://batmilk.herokuapp.com/new'

response = requests.post(url=url, params={'password': password, 'name': data['name'], 'text': data['text']})

print(response)

url = 'https://batmilk.herokuapp.com/%s/new-contender' % data['name']

for name in data['contenders']:
    response = requests.post(url=url, params={'password': password, 'name': name})
    print(response)

