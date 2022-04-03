import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect",allow_redirects=True)
x = len(response.history)
last_response = response.history[x-1]

print(f"The redirect happens {x}  times")
print(last_response.url)
