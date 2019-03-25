import requests
import logging

log = logging.getLogger(__name__)

def get_all_works():
    url = 'https://api.datacite.org/works'
    headers = {'Content-Type': 'application/json'}
    params = '?data-center-id=snd.bils'
    response = requests.get(url + params, headers=headers)
    assert response.status_code == 200
    works_array = []

    for item in response.json()['data']:
        work_dict = dict()
        work_dict['title']=item['attributes']['title']
        work_dict['description']=item['attributes']['description']
        work_dict['year']=item['attributes']['published']
        work_dict['doi']=item['attributes']['doi']
        work_dict['access_constraints']=item['attributes']['license']
        work_dict['authors']=item['attributes']['author']
        works_array.append(work_dict)

    return works_array

def get_work_by_id(doi):
    url = 'https://api.datacite.org/works'
    headers = {'Content-Type': 'application/json'}
    params = r'?query=doi:{}&data-center-id=snd.bils'.format(doi)
    log.info(params)
    response = requests.get(url + params, headers=headers)
    assert response.status_code == 200
    work_dict = dict()

    for item in response.json()['data']:
        work_dict['title']=item['attributes']['title']
        work_dict['description']=item['attributes']['description']
        work_dict['year']=item['attributes']['published']
        work_dict['doi']=item['attributes']['doi']
        work_dict['access_constraints']=item['attributes']['license']
        work_dict['authors']=item['attributes']['author']

    return work_dict