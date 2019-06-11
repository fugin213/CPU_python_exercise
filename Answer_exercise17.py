import urllib.request as req
import json

url="https://blockchain.info/rawaddr/1AKpfwYmBUYfRAkFvgMWLeJxJXFHdu1DCT"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
})

with req.urlopen(request) as response:
    reqjson=json.load(response)
#    print(reqjson["txs"][0]["inputs"][0]["prev_out"]["addr"])

    for i in range(len(reqjson)):
        for j in range(len(reqjson["txs"][i]["inputs"])):
                 print(reqjson["txs"][i]["inputs"][j]["prev_out"]["addr"])

