b_split=[]
fr=open("read.txt","r")
a=fr.read()
print("The content of the file is:" , a)
b_split=a.split(" ")
#print(b_split)
b=[2,3,4,5,3,2,4]
fw=open("write.txt","w")
for i in range(len(b)):
    fw.writelines(str(b[i])+" ")
    print(str(b[i])+" is written to the file")
fw.write("\n")