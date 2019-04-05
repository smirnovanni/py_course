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
    answer = requests.get(API_URL + '/result', req)
    if answer.json()['status'] == 'success':
        return answer.json()['response']
    else:
        return answer.json()['exception']