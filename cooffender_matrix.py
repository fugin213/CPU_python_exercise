import csv
case=[]
criminal=[]
cooffender=[]
criminal_co=[]

with open ("來源檔案名稱") as csvfile:
    rows=csv.reader(csvfile)
    data=list(rows)

    for i in range(len(data)):
        if data[i][0] not in case:
            case.append(data[i][0])
        if data[i][1] not in criminal:
            criminal.append(data[i][1])

csvfile.close()

with open ("目的檔案名稱", "w") as csvwrite:
    csvwrite.write(",")
    for i in range(len(criminal)):
        csvwrite.write(criminal[i]+",")
    csvwrite.write("\n")

    for p in range(len(criminal)):
        csvwrite.write(criminal[p]+",")
        criminal_co=criminal.copy()
        cooffender.clear()
        for i in range(len(criminal_co)):
             criminal_co[i]=0
        
        for j in range(len(data)):
            if criminal[p]==data[j][1]:
                casenumber=data[j][0]
                for k in range(len(data)):
                    if data[k][0]==casenumber and criminal[p]!=data[k][1]:
                        cooffender.append(data[k][1])
                        print("casenumber:"+ casenumber+" ,criminal:"+ criminal[p]+" ,cooffender:"+str(cooffender))
                        for l in range(len(criminal)):
                            if criminal[l] in cooffender:
                                criminal_co[l]='1'
                            else:
                                criminal_co[l]='0'
    
        
        for q in range(len(criminal_co)):
            csvwrite.write(str(criminal_co[q])+",")
        csvwrite.write("\n")

csvwrite.close()

