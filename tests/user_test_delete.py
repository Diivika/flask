from requests import delete, get

print(delete('http://localhost:8080/api/users/999').json())
# новости с id = 999 нет в базе
print(delete('http://localhost:8080/api/users/awfafafaf').json())
print(delete('http://localhost:8080/api/users/1').json())

print(get('http://localhost:8080/api/users').json())

# v2
print(delete('http://localhost:8080/api/v2/users/2').json())
print(delete('http://localhost:8080/api/v2/users/999').json())
print(delete('http://localhost:8080/api/v2/users/svssvsvvs').json())

print(get('http://localhost:8080/api/users').json())