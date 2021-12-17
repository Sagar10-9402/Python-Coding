while True:
    
    try:
        age = int(input("Enter your age :"))
        break
    except ValueError:
        print("invalid input")
        

    
if age < 18:
    print("sorry u cant play this game ")
else:
    print("welcome")    
    
