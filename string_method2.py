#strip method 
#find method
#replace method 
#center method 

#strip method ( in this method we are delete the spaces )
Name = "     sagar   "
dots = ".............."
print(Name +dots)
print(Name.strip() + dots )

#find method (in find method we are find the position of that word )
Name =" karan is a good dancer "

print(Name.find("is"))

#replace method 

print(Name.replace("is","was"))


Name = "Sagar"

print(Name.center(9,"*"))

Name =input("Enter your name : ")

print(Name.center(len(Name) +4,"*"))
