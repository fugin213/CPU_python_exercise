import string
s_old=input("Please enter a sentence:")
print("The original string is: ", s_old)
reverse_s=""
s=s_old.replace('.','')
split_s=s.split()
reverse_list=[]
for i in range(len(split_s)):
    reverse_list.append(split_s[len(split_s)-i-1])

for i in range(len(reverse_list)):
    reverse_s=reverse_s+reverse_list[i]+' '

print("The reversed string is: ", reverse_s)
