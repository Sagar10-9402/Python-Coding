#for loop
#total of sum num

total =0

for i in range(10):
   # print(f"hello : {i}")
    total += i
    
print(total)


#input from the user 

no = int(input("enter your no : "))
 
total = 0
for i in range(1,no+1):
 	 	total += i 
print(total)


#using indexing for sum

no=(input("enter a number :"))

total = 0

for i in range(0,len(no)):
	total += int(no[i])
print(total)