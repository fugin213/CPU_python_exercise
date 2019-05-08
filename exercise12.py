
import string
a=[]
f=open("read.txt","r")
rf=f.read()
rf_split=rf.split(" ")
for i in range(len(rf_split)):
         a.append(int(rf_split[i]))

#a=list(map(int,rf_split))
print(a)
sort=[]
temp_max=0
for i in range(len(a)):
    if a[i]>=temp_max:
        temp_max=a[i]

for i in range(temp_max+1):
    for j in range(len(a)):
        if a[j]==i:
            sort.append(a[j])
           

fw=open("sort.txt","w")
for i in range(len(sort)):
        fw.write(str(sort[i])+" ")
        
print(sort)


