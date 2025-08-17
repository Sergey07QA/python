import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '667556ad8ccbdb642ced81f4b4e6eee0'
header= {'Content-Type': 'application/json', 'trainer_token':token}
trainer_id = '38442'


def test_status_code():
    response = requests.get(url=f'{url}/pokemons', params={'trainer_id': trainer_id})
    assert response.status_code==200


def test_part_of_response():
    response_get = requests.get(url=f'{url}/pokemons', params={'trainer_id': trainer_id})
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'