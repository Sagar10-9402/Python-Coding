#################
l=[]
for i in range(1,4):
    n=input(" input :")    
    l.append(n)
print(l)    
########################

n=input("enter your string")
l=n.split()
print(l)

#################

s='sagar gorakh phule'
words = []
word = ""
for chara in s:
    if chara == " ":
        words.append(word)
        word = ""
    else:
        word += chara
else:
    words.append(word)

print(words)