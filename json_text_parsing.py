import json

string_as_json_foramt = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(string_as_json_foramt)
obj1 =obj['messages']
obj2 =obj1[len(obj1)-1]


key = "message"
if key in obj2:
    print(obj2['message'])
else:
    print(f"The key {key} in JSON not found")