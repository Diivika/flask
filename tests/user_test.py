from requests import get

print(get('http://localhost:8080/api/users').json())
print(get('http://localhost:8080/api/users/1').json())
print(get('http://localhost:8080/api/users/999').json())
print(get('http://localhost:8080/api/users/svssvsvvs').json())


# v2
print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/1').json())
print(get('http://localhost:8080/api/v2/users/999').json())
print(get('http://localhost:8080/api/v2/users/svssvsvvs').json())