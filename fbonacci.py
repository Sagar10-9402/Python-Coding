# fibonachi series
def fibonacci_seres(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(b)    
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end= ' ')
            
            
fibonacci_seres(10)                        
            

