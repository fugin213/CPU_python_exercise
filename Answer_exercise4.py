x=input("please enter a number: ")
x=int(x)
divisor=[]
for i in range(x):
    if x%(i+1)==0:
        divisor.append(i+1)


print(divisor)
