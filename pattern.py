# pattern 

n= int (input("enter a num:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("2",end=" ")
    print()    
    
# output
# 2 
# 2 2
# 2 2 2
# 2 2 2 2
# 2 2 2 2 2
    

n=int(input( "Enter a input no:"))
k = 2* n - 1
for i in range (0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):    
        print("*",end=" ")    
    print()
    
#    output
   
    #      * 
    #     * *
    #    * * *
    #   * * * *
    #  * * * * *

n=int(input("enter your no :"))
k=2*n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
        
    k=k-1
    for j in range(0,i+1):
        print("*",end="")
    print()    
    

    # output
    #      *
    #     **
    #    ***
    #   ****
    #  *****    
    
    
    
    
    
    
    