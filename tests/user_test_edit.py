from requests import get, put

print(put('http://localhost:8080/api/users/2', json={}).json())

print(put('http://localhost:8080/api/users/2',
           json={'name': 'asfafafasfasfas'}).json())

print(put('http://localhost:8080/api/users/2',
           json={'surname': 'Sigmason',
                 'name': 'Sanya',
                 'age': 77,
                 'position': 'pilot-2',
                 'email': 'superpilot2@mars.space',
                 'address': 'module_2',
                 'password': 'sigmawork2',
                 'speciality': 'pilot_support',
                 'city_from': 'Samara'}).json())

print(get('http://localhost:8080/api/users').json())

# v2

print(put('http://localhost:8080/api/v2/users/1', json={}).json())

print(put('http://localhost:8080/api/v2/users/1',
           json={'name': 'asfafafasfasfas'}).json())

print(put('http://localhost:8080/api/v2/users/3',
           json={'surname': 'Sigmason',
                 'name': 'Sanya',
                 'age': 77,
                 'position': 'pilot-2',
                 'email': 'superpilot2@mars.space',
                 'address': 'module_2',
                 'password': 'sigmawork2',
                 'speciality': 'pilot_support',
                 'city_from': 'Samara'}).json())

print(get('http://localhost:8080/api/v2/users').json())