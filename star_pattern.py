from typing import Pattern


row=int(input("enter your digit :"))
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="  ")
    for j in range (1,i+1):
        print("1",end=" ")   
    print()     


# output    
# *  1 
# *  *  1 1
# *  *  *  1 1 1
# *  *  *  *  1 1 1 1
# *  *  *  *  *  1 1 1 1 1
######################


# num Pattern single digit 
def num(n):
    k=2*n+1
    for i in range(0,n):
        for j in range(0,k):
            print(end='')
        for j in range(0,i+1):
            print(n,end=' ')
        print()
num(4)             


# output
# 4
# 4 4
# 4 4 4
# 4 4 4 4




rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')   
        

# output
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5        


rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')


# output    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# reverce Pattern
rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
   
# output     
# 1
# 2 1
# 3 2 1 
# 4 3 2 1
# 5 4 3 2 1


# mostly askd que 

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()

# output
# 1
# 2  4
# 3  6  9
# 4  8  12  16
# 5  10  15  20  25
# 6  12  18  24  30  36
# 7  14  21  28  35  42  49
# 8  16  24  32  40  48  56  64

    
# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")


# output
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

