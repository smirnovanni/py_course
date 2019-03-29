import json

import requests

url = 'https://api.github.com'

print('Запрос')
req = {'username': 'smirnovanni'}

print(json.dumps(req, sort_keys=True, indent=4))

ans = requests.post(url, req)
print('\n\n')

print('Ответ')
print(json.dumps(ans.json(), sort_keys=True, indent=4))
