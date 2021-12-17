from collections import Counter
import collections
def LetterCount(text):
    return Counter(c for c in text.lower() if c.isalpha())

print(LetterCount ("Hello there"))

####################################################################################################


s=input('enter your string hear :')
d={}
for letter in s:
    if letter in d:
        d[letter]+=1
    else:
        d[letter]=1
print(d)        
            
{'m': 2, 'y': 1, ' ': 3, 'n': 1, 'a': 3, 'e': 1, 'i': 1, 's': 2, 'g': 1, 'r': 1}

########################################################### chara count how many chara is lower and upper case ###############

s = "Sagar"
l,u = 0,0
for i in s:
    if (i>='a'and i<='z'):
          
        # counting lower case
        l=l+1                 
    if (i>='A'and i<='Z'):
          
        #counting upper case
        u=u+1   
print('Lower case characters: ',l)
print('Upper case characters: ',u)

# Lower case characters:  4
# Upper case characters:  1

###############################################################



s1 = "my name is sagar"

d={}
for i in s1:
    if s1 in d:
        d[i]+=1
    else:
        d[i]=1
print(d)        



