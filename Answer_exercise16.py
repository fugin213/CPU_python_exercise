import urllib.request as req
import bs4

url="https://www.cpu.edu.tw/bin/home.php"
request=req.Request(url)
response=req.urlopen(request)
data=str(response.read(),"utf-8")

root=bs4.BeautifulSoup(data,"html.parser")
links=root.find_all("a")
# print(links)
for link in links:
    if link.string!=None:
        print(link.string)
