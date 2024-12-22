import requests


payload = {"method": "GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.request("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload)
print(response.text)

