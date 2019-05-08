word=input("plese enter a word: ")
print("Your word is : ", word)
for i in range(len(word)):
    if word[i]==word[len(word)-i-1]:
        if i==len(word)-1:
            print("reversible")
            continue
    else:
        print("not resersible")
        break
    