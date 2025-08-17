import requests

url = 'https://api.pokemonbattle.ru/v2'

token = '667556ad8ccbdb642ced81f4b4e6eee0'
header= {'Content-Type': 'application/json', 'trainer_token':token}
body_registration = {
    "trainer_token": token,
    "email": "Karnauhov-sv@yandex.ru",
    "password": "qWerty123",
    "password_re": "qWerty123"
    }
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
    }

body_add_pokeballs = {
    "pokemon_id": ['id']
}



'''response = requests.post(url=f'{url}/trainers/reg', headers=header, json=body_registration)
print(response.text)'''

response_create =requests.post(url=f'{url}/pokemons', headers=header, json = body_create)
print(response_create.json())

message = response_create.json()['message']
print(message)

response_add_pokeball =requests.post(url=f'{url}/trainers/add_pokeball', headers=header, json = body_add_pokeballs)
print(response_add_pokeball.text)
