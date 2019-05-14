while 1==1:
    x=input("please enter a number: ")
    x=int(x)
    tag=0
    if (x==1):
        tag=2

    for i in range(x):
        if (i!=0 & i!=x):
            if (i!=1):
                if x%i!=0:
                    continue
                else:
                    tag=1

    if tag==0:
        print("This is a prime number!")
    elif tag==2:
        print("1 is not a prime number!")
    else:
        print("This is not a prime number")
