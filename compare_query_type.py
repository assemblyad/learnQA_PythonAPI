from json import JSONDecodeError

import requests
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

payload = {"method": ""}
response = requests.get("https://playground.learnqa.ru/api/compare_query_type",params=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": ""}
response = requests.post("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": ""}
response = requests.put("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": ""}
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
payload = {"method": "HEAD"}
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type",params=payload)
print(f"выводиться в этом случае {response.text}")
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

payload = {"method": "GET"}
response = requests.get("https://playground.learnqa.ru/api/compare_query_type",params=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": "PUT"}
response = requests.put("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

payload = {"method": "DELETE"}
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type",data=payload)
print(f"выводиться в этом случае {response.text}")

"""
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
   Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
   И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.
   Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
"""
all_method_types =['GET','POST','PUT','DELETE']

for item in all_method_types:
    payload = {"method": item}

    headers = {"method": "DELETE"}
    response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data=payload,headers=headers)

    try:
        response.json()
        if item != response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} не совпадает со значением параметра {item}, сервер отвечает так, словно все ок")

    except JSONDecodeError:
        if item == response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} совпадает со значением параметра {item}, типы совпадают, но сервер считает, что это не так")

    headers = {"method": "POST"}
    response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data=payload,headers=headers)

    try:
        response.json()
        if item != response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} не совпадает со значением параметра {item}, сервер отвечает так, словно все ок")

    except JSONDecodeError:
        if item == response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} совпадает со значением параметра {item}, типы совпадают, но сервер считает, что это не так")

    headers = {"method": "PUT"}
    response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data=payload,headers=headers)

    try:
        response.json()
        if item != response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} не совпадает со значением параметра {item}, сервер отвечает так, словно все ок")

    except JSONDecodeError:
        if item == response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} совпадает со значением параметра {item}, типы совпадают, но сервер считает, что это не так")


    headers = {"method": "DELETE"}
    response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data=payload,headers=headers)

    try:
        response.json()
        if item != response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} не совпадает со значением параметра {item}, сервер отвечает так, словно все ок")

    except JSONDecodeError:
        if item == response.request.headers['method']:
            print(f"сочетание, когда реальный тип запроса {response.request.headers['method']} совпадает со значением параметра {item}, типы совпадают, но сервер считает, что это не так")