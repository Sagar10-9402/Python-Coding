# how to use "if"condition 

Age =int(input("Enter your Age :")) 

if Age >= 18:

	print("your age is above 18")
	print("welcome ")

else:
	print("soryy, cant play the Game ")	


#pass statement

x = 18

if x > 18:
	pass




#gusssing game
wining_no = 42 
no =int(input(print("gusssing your no :")))

if no == wining_no:
	
	print("you win")

else:
	if no < wining_no:
		print("to low")	
	else:
		print("to high")
