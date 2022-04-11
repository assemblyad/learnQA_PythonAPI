from json import JSONDecodeError
import json
import requests
import time

payload = {"token": ""}
seconds_key = "seconds"
token_key = "token"
status_key = "status"
result_key = "result"
wait_time = 0

# 1) создавал задачу
try:
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    obj = response.json()

    if seconds_key in obj:
        wait_time = obj[seconds_key]
        print(obj[seconds_key])
    else:
        print(f"The key {seconds_key} in JSON not found")

    if token_key in obj:
        #print(obj[token_key])
        payload = {"token": obj[token_key]}
    else:
        print(f"The key {token_key} in JSON not found")
    
    #print(f"выводиться в этом случае {response.text}")


except JSONDecodeError:
        print(f"JSON parse failed because this is not JSON format")

#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status

try:
    #print(payload)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    obj = response.json()

    if status_key in obj:
        if obj[status_key] =="Job is NOT ready":
            print(obj[status_key])
    else:
        print(f"The key {status_key} in JSON not found")

    #print(f"выводиться в этом случае {response.text}")

except JSONDecodeError:
    print(f"JSON parse failed because this is not JSON format")

#3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
time.sleep(wait_time)
#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

try:
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    obj = response.json()

    if status_key in obj:
        if obj[status_key] == "Job is ready":
            print("Job is ready")
    else:
        print(f"The key {status_key} in JSON not found")

    if result_key in obj:
        if result_key is not None:
            print(obj[result_key])
    else:
        print(f"The key {result_key} in JSON not found")

    #print(f"выводиться в этом случае {response.text}")

except JSONDecodeError:
    print(f"JSON parse failed because this is not JSON format")
