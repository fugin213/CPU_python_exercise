x=input("How many Fibonacci number do you want to generat? ")
x=int(x)
fib=[0,1]
if x==0:
    print("You need to generate at list one Fibonacci numbers!")
elif x==1:
    print(fib[1])
elif x>1:
    for i in range(x+1):
        if i>1:
            fib.append(fib[i-1]+fib[i-2])
print(fib[1:x+1])
