import json
from django.http import JsonResponse
import requests

# endpoint = "http://127.0.0.1:8000/apis/195/,para"

# response = requests.post('http://127.0.0.1:8000/apis/', data={'emp_id':'204','first_name':'Aryan','last_name':'Primta','dob':'2001-09-22','salary':'70000','address':'Solan, Himachal Pradesh','role':'SDE','doj':'2024-10-10'})
# 
# response = requests.get('http://127.0.0.1:8000/apis/197')

# response = requests.delete('http://127.0.0.1:8000/apis/204')

response = requests.put('http://127.0.0.1:8000/apis/197', data = {'first_name':'Aryan'})

print(response.content)