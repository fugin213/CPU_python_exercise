s1=[1,3,5,7,9]
print(s1)
s1.append(10)
print(s1)

s2=[2,4,6,8,10]
print(s2)

s2.insert(0,0)
print(s2)

s4=list(set(s1).intersection(set(s2)))
s5=list(set(s1).union(set(s2)))

print("the intersection of s1 and s2 is : ", s4 )
print("the union of s1 and s2 is : ", s5)
