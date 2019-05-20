from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

newstoken_noncap=[]
newstoken_noncapstem=[]
keywords_count=[]
keywords=set()
keywordslist=[]
toprankkeywords=[]
count=0

#讀取news檔案
with open("news.txt", mode="r") as f:
        rf=f.read()

newstoken=rf.split()

#去除特殊符號
string1=rf.replace('\n', '')
string2=string1.replace('"','')
string3=string2.replace('.','')
string4=string3.replace(',','')
string5=string4.replace('(','')
string6=string5.replace(')','')
string7=string6.replace("'",'')
string8=string7.replace('-','')

#文章轉換成單字(tokenize)，以空白分格
newstoken=string8.split(" ")

#把大寫字母轉換成小寫再存成另一個newstoken_filter list
for i in range(len(newstoken)):
        newstoken_noncap.append(newstoken[i].lower())

#讀取stopword檔，並將單字內容存成list
f=open("stopwords.txt","r")
rf=f.read()
f.close
stopwords=rf.split("\n")

count=0
#把newstoken_filter符合stopwords的字移除
for i in range(len(newstoken)):
        for j in range(len(stopwords)):
                if newstoken[i]==stopwords[j]:
                        newstoken_noncap.remove(newstoken[i])

ps = PorterStemmer() 

#將文章內的字儲存在set內，去除重複字，並將字還原成字根(這部分可以先省略不看)
for i in range(len(newstoken_noncap)):
        newstoken_noncapstem.append(ps.stem(newstoken_noncap[i]))
        keywords.add(ps.stem(newstoken_noncap[i]))

#把set存成list以利後續操作
keywordslist=list(keywords)

#創造一個list用來儲存每個單字出現的次數
keywords_count=[0]*len(keywordslist)

#計算每個單字出現的次數，記錄在keywords_count中
for i in range(len(newstoken_noncapstem)):
        for j in range(len(keywordslist)):
                if newstoken_noncapstem[i]==keywordslist[j]:
                        keywords_count[j]+=1


top=5
count=0
#用2個for迴圈，記錄出現頻率前5名的單字
while count<top:
        max=0
        for i in range(len(keywords_count)):
                if keywords_count[i]>max:
                        max=keywords_count[i]
        
        for i in range(len(keywordslist)):
                if keywords_count[i]==max:
                        toprankkeywords.append(i)
                        keywords_count[i]=0
                        count+=1


for i in range(len(toprankkeywords)):
        print(keywordslist[toprankkeywords[i]])