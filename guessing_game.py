#gussing game 


Win_no = 25
No =int(input("guess the no b/w 1 to 100 :"))

if No == Win_no:
	print("YOU WIN!!!")

else:
	if No < Win_no:
		print("To low")
	else:
		print("To high")
