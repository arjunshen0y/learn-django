import requests

url = 'http://127.0.0.1:8000/books/'
headers = {'Authorization': 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MTQyNTQ4LCJqdGkiOiJjYjY1MzQ1OTA1NTk0NzQxYWEwMGY5NDU0Y2EwMTI5YSIsInVzZXJfaWQiOjF9.L0AMp9dL6R2Vlr-fQYWiWFv2-7EboYGQDjZdDTknsg4'}
r = requests.get(url, headers=headers)

print(r.text)