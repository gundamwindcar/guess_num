import random

r = random.randint(1,100)
count = 0

while True:
	guess = input('Please guess the number:')
	guess = int(guess)
	count += 1
	if guess == r:
		print('Congratulations! You got the number!')
		break
	elif guess > r:
		print('Your guess is larger than the number')
	elif guess < r:
		print('Your guess is smaller than the number')
	print('Times of guess:', count)