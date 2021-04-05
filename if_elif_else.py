#Ticking 
#age 0-3 prise free
#age 4 to 10 prise 100
#age 10 to 60 prise 150
#age above 60 prise 200


Age=int(input("enter your age"))
if Age==0:
	print("you cant watch ")


elif 0<Age<=3:
	print("Tikit prise is : free")

elif 4<Age<=10:
	print("Tikit prise is : 100 ")
elif 10<Age<=60:
	print("Tikit prise is : 150 ")	

else:
	print("tikit prise is : 200 ")