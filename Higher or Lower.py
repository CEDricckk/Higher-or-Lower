#Higher or Lower
import random
num1 = random.randint(1, 50)
tryAgain = 1
attempt = 0

#Loop
while tryAgain == True:
	tryAgain = False
	num2 = int(input('guess the number! '))
	if num1 < num2:
		print('Lower')
		tryAgain = True
		attempt = attempt +  1
	elif num1 > num2:
		print('Higher')
		tryAgain = True
		attempt = attempt + 1
	elif num1 == num2:
		tryAgain = 0
		print(f'You did {attempt} attempts')
		
#last part
roast = ['my grandpa beats this with his eyes closed', 'get gud', 'are you even trying?', 'dont play this game anymore']
if attempt <= 5:
	print('Amazing')
elif attempt <= 10:
	print('Great! you are above average')
elif attempt <= 15:
	print('You did it but you need more practice')
elif attempt > 15:
	print(roast[random.randint(0, 3)])
	