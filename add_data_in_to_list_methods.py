#how to add itoms in list 
#append method= we can use for the add itoms in the list

name=[]
name.append('sagar')
name.append('phule')
print(name)

#we r also add the itom in list

name=['mango','apple']
name.append("graps")
print(name)
####################----------###############
#methons used for add the data in th list 
#1 append method 
#2 insert method 
#3 extend method 
#####################---------################


#1 append method 


fruits =[]
fruits.append('graps')
fruits.append('mango')
print(fruits)


fruits=['mango ']
fruits.append('graps')
print(fruits)


#2 insert method 

fruits = ["graps"]
fruits.insert(0, 'apple')
print(fruits)

#extend method

fruits1 =["mango","apple",]
fruits2 = ["graps"]
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)



#simple additon 


fruits1=["apple"]
fruits2=["mango"]

fruits=fruits1 + fruits2
print(fruits)