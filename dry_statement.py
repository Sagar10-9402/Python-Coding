# dry statement = dont repeat your self  meaning is try to avoide max no of coding lines  

import random
win_no = random.randint(1,100)
no = int(input("ENTER YOUR NO B/W 1 TO 100 :"))
#win_no = 1
game_over = False
guess = 1



while not game_over:
		if  no== win_no:
			print(f"YOU WIN ! , your guessing in {guess} times")
			game_over= True
		else:
			
			if no<win_no:
				print(" to low ")
			else:
				print("to high")	
		no =int(input("Enter no :"))
		guess += 1
			
