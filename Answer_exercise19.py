import json

with open("parking.json", encoding='utf-8-sig') as file:
    p_json=json.load(file)
parking=p_json["parkingLots"]
# print(parking[0]["parkName"])

for i in range(len(parking)):
    print(parking[i]["parkName"])
# for addr in parking:
#     print(addr["address"])