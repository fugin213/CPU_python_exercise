b=[2,3,4,5,3,2,4]
fw=open("write.txt","w")
for i in range(len(b)):
    fw.writelines(str(b[i])+" ")
    print(str(b[i])+" is written to the file")
fw.write("\n")