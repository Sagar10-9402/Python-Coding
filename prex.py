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