import urllib.request as req
url="https://www.blockchain.com/btc/tx/1c12443203a48f42cdf7b1acee5b4b1c1fedc144cb909a3bf5edbffafb0cd204"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read()
    #fw=open("bitcointrans.txt","w")
    #fw.write(str(data))
    #fw.close

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
accounts=root.find_all("a")

#print(accounts)
for account in accounts:
    address=str(account)
    if "address" in address:
        print(account.string)

