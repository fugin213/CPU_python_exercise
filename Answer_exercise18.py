import json

with open("bicycle.json", encoding="utf-8") as file:
    p_json=json.load(file)

records=p_json["result"]["records"]
for addr in records:
    print(addr["sna"])