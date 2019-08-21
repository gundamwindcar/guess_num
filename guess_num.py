import random

r = random.randint(1,100)
while True:
	guess = input('Please guess the number:')
	guess = int(guess)
	if guess == r:
		print('Congratulations! You got the number!')
		break
	elif guess > r:
		print('Your guess is larger than the number')
	elif guess < r:
		print('Your guess is smaller than the number')

