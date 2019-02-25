import random

p = 0
d = 0

snl={8:37,38:9,11:2,13:34,40:68,65:46,52:81,76:97,65:46,93:63,89:70}
def rolldice():
	return random.randint(1,6)

while True:
	r = input("press r to roll the dice, q to quit : ")
	if r == 'r':
		d = rolldice()
		print("you got",d)

		if d ==  6 or d == 1 :
			print("congratulations, you're in the game!")
			break
		else:
			print("you need to get 6 or 1 to start. try again. ")
	elif r == 'q':
		exit()
while True:
	r = input("press r to roll the dice, q to quit : ")
	if r == 'r':
		d = rolldice()
		print("you got",d)
		p = p+d
		if p == 100:
			print("hurry! you won!")
			exit()
		if p > 100:
			p = p - d
			print("you need to get",100-p,"to reach home. ")
		print("your new position is ",p)
		if p in snl:
			if p < snl[p]:
				print("you got a ladder.")
			else:
				print("oops, you got swallowed by a huge snake.")

			p = snl[p]
			print("move to ",p)
	elif r == 'q':
		exit()
		