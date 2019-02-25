import random
l=["r", "p", "s"]
while True:
	u=input("enter your choice,or press n to exit : ")
	if u=='n':
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses",c)

	if u==c :
		print("tie")
	elif u=="r" and c=="p" :
		print("computer wins")

	elif u=="r" and c=="p" :
		print("computer wins")	
	elif u=="p" and c=="r" :
		print("you win")

	elif u=="s" and c=="r" :
		print("computer wins")
	elif u=="r" and u=="s" :
		print("you win")


	elif u=="p" and c=="s" :
		print("computer wins")
	elif u=="s" and u=="p" :
		print("you win")


	