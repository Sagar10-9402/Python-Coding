

# s1=int(input("enter a first no "))
# s2 = int(input("enter a second no "))

# for num in range (s1,s2+1):
#     if num >1:
#         for i in range (2,num):
#             if num%2==0:
#                 break
#         else :
#                 print(num,end=' ')


# find the prime no 
# def primenum(no):
#     for i in range(2,no):
#         if no % 2==0:
#             print("this no is not a prime ")
#             break

#     else:
#         print("prime no")        

# no = int(input('enter a no :'))
#20
# print(primenum(int(input('enter a no :'))))



# we can define prime no like this 

def primeNo(n):
    for i in range(2,n):
        if n%2==0:
            print("no")
            break
    else:
        print("yes")        
    
primeNo(9)    



