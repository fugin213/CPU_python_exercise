newstoken_filter=[]
newstoken_noncap=[]

#讀取news檔案
with open("news.txt", mode="r") as f:
        rf=f.read()

#切割單字
newstoken=rf.split(" ")

#把大寫字母轉換成小寫再存成另一個newstoken_noncap list
for i in range(len(newstoken)):
        newstoken_noncap.append(newstoken[i].lower())

#複製newstoken_noncap內容至另一個新list newstoken_filter
newstoken_filter=newstoken_noncap.copy()

#讀取stopword檔，並將單字內容存成list
f=open("stopwords.txt","r")
rf=f.read()
f.close
stopwords=rf.split("\n")

#把newstoken_filter符合stopwords的字移除
for i in range(len(newstoken)):
        for j in range(len(stopwords)):
                if newstoken_noncap[i]==stopwords[j]:
                   newstoken_filter.remove(newstoken_noncap[i])

#印出去除stopwords的單字及數量
print(newstoken_filter)
print(len(newstoken_filter))

