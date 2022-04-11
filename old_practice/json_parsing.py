import json

string_as_json_foramt = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_foramt)
#print(obj['answer'])

key = "answer"
if key in obj:
    print(obj[key])
else:
    print(f"The key {key} in JSON not found")