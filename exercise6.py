import random
a=random.randint(1,9,)
print("the answer is: ",a)
i=int(input("please enter your answer: "))
if a==i:
    print("bingo")
while(a!=i):
    if i<a:
        print("too small, try again!")
        i=int(input("please guess again: "))
        continue
    else:
        print("too big, try again!")
        i=int(input("please guess again: "))
        continue
print("bingo")
