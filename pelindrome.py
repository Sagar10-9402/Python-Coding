def pelindrome(word):
    if word in word[::-1]:
        return True 
    else:
        return False 

word = input("enter your word ")
print(pelindrome(word))    

# word = input(" Enter your word : ")
# word_count= ''
# while word!=True:
   
#     if word in word[::-1]:
#         print("True")
#         word_count+=word 
#     else:
#         print('false')   
    
# word ==False        




