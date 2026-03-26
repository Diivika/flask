from requests import delete, get

print(delete('http://localhost:8080/api/jobs/999').json())
# новости с id = 999 нет в базе
print(delete('http://localhost:8080/api/jobs/awfafafaf').json())
print(delete('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs').json())