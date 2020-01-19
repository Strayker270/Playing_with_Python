import random

random_number = random.randint(1,25)
i = None

while True:
	i = input("Guess a number from 1 to 25: ")
	i = int(i)
	if i > random_number:
		print("It's to high!")
	elif i < random_number:
		print("It's to low!")
	else:
		print("You win!")
		again = input("Wish to play again? y/n: ")
		if again == "y":
			random_number = random.randint(1,10)
			i = None
		else:
			print("Thanks for playing!")
			break


