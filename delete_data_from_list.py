#delete data in the list

# 3 types to delete the data from list

##---------------------------##

#pop method is used to delete the last word of string 

####### pop method 

fruits=["mango",'banana', 'apple','watermelon']
fruits.pop()
print(fruits)

#######  remove method ########


fruits=["mango",'banana', 'apple','watermelon']
fruits.remove("banana")
print(fruits)

######m  delete fun   #########


fruits=["mango",'banana', 'apple','watermelon']
del fruits[2]
print(fruits)