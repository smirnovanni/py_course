import requests

API_KEY = 'cHGk0u8XIFM1'
API_URL = 'https://api-ip.fssprus.ru/api/v1.0'


def send_req(**kwargs):
    region = kwargs['region']
    firstname = kwargs['firstname']
    lastname = kwargs['lastname']
    secondname = kwargs['secondname']
    birthdate = kwargs['birthdate']
    req = {'token': API_KEY, 'region': region, 'firstname ': firstname, 'lastname  ': lastname,
           'secondname': secondname, 'birthdate': birthdate}
    answer = requests.get(API_URL + '/search/physical', req)
    if answer.json()['status'] == 'success':
        return answer.json()['response']['task']
    else:
        return answer.json()['exception']


def get_status(task):
    req = {'token': API_KEY, 'task': task}
    answer = requests.get(API_URL + '/status', req)
    if answer.json()['status'] == 'success':
        return answer.json()['code']
    else:
        return answer.json()['exception']


def get_result(task):
    req = {'token': API_KEY, 'task': task}
    answer = requests.get(API_URL + '/status', req)
    if answer.json()['status'] == 'success':
        return answer.json()['response']
    else:
        return answer.json()['exception']

#r = send_req(region=None, firstname='Сергей', lastname='Соколов', secondname=None, birthdate=None)
#print(r)
#d = get_status(r)
#print(d)
f = get_result('e08a075b-6f5e-4386-b3ba-2948ad6657bd')
print(f)