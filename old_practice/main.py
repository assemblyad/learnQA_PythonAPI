from json.decoder import JSONDecodeError
import requests
"""
payload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello",params=payload)
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/check_type",params={"param1": "value1"})
print(response.text)


response = requests.post("https://playground.learnqa.ru/api/check_type",data={"param1": "value1"})
print(response.text)

payload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello",params=payload)
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/hello",params={"name": "User"})
parsed_response_text = response.json();
print(parsed_response_text)
print(parsed_response_text["answer"])

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
 

response = requests.post("https://i1cqoys68c-dsn.algolia.net/1/indexes/stg_choicemarket_products/query?x-algolia-application-id=I1CQOYS68C&x-algolia-api-key=eac7b807c0109771a245855c7501fca3",data='{"params":"query=chicken&hitsPerPage=5"}')
#print(response.text)

response = requests.post("https://i1cqoys68c-dsn.algolia.net/1/indexes/stg_choicemarket_products/query?x-algolia-application-id=I1CQOYS68C&x-algolia-api-key=eac7b807c0109771a245855c7501fca3",data='{"params":"query=chicken&hitsPerPage=5"}')
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)


response = requests.post("https://playground.learnqa.ru/api/get_301",allow_redirects=False)
print(response.status_code)
#print(response.text)
"""

response = requests.post("https://playground.learnqa.ru/api/get_301",allow_redirects=True)
first_response = response.history[0]
second_response = response
print(first_response.url)
print(second_response.url)

