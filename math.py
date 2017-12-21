import random
from decimal import *

def choose(term):
	return term in ['rock', 'paper', 'scissors']
def analysis(filename):
	File = open(filename, 'r')
	words = File.read().split(" ")
	rockCount = 0
	paperCount = 0
	scissorsCount = 0
	for word in words:
		if word == 'rock':
			rockCount+=1
		if word == 'paper':
			paperCount+=1
		if word == 'scissors':
			scissorsCount+=1
	File.close()
	return rockCount, paperCount, scissorsCount
def gameFunction(filename, rockCount, paperCount, scissorsCount):
	newFile = open(filename, 'ar')
	totalGames = rockCount + paperCount + scissorsCount
	rockPercentage = (Decimal(rockCount)/Decimal(totalGames)) * 100 
	paperPercentage = (Decimal(paperCount)/Decimal(totalGames)) * 100 
	scissorsPercentage = (Decimal(scissorsCount)/Decimal(totalGames)) * 100 
	print "We have played " + str(totalGames) + " times"
	print "You have chosen rock " + str(rockCount) + " times"
	print "You have chosen paper " + str(paperCount) + " times"
	print "You have chosen scissors " + str(scissorsCount) + " times"
	
	userInput = ''
	computerInput = ['rock', 'paper', 'scissors']
	if rockPercentage > paperPercentage and rockPercentage > scissorsPercentage:
		computerInput = ['paper']
	if paperPercentage > rockPercentage and paperPercentage > scissorsPercentage:
		computerInput = ['scissors']
	if scissorsPercentage > paperPercentage and scissorsPercentage > rockPercentage:
		computerInput = ['rock']
	computerChoice = random.choice(computerInput)
	while not choose(userInput):
		userInput = raw_input("Enter 'rock', 'paper', or 'scissors': ")
		if not choose(userInput):
			try:
				i = int(userInput)
				newFile.write(userInput + ' ')
			except ValueError as e:
				print('Invalid input: please reenter')
		else:
				newFile.write(userInput + ' ')
				print("The computer chose " + computerChoice)
				if(computerChoice == 'rock' and userInput == 'paper'):
					print("YOU WIN")
				if(computerChoice == 'paper' and userInput == 'scissors'):
					print("YOU WIN")
				if(computerChoice == 'scissors' and userInput == 'rock'):
					print("YOU WIN")
				if(computerChoice == 'rock' and userInput == 'scissors'):
					print("THE COMPUTER WINS")
				if(computerChoice == 'paper' and userInput == 'rock'):
					print("THE COMPUTER WINS")
				if(computerChoice == 'scissors' and userInput == 'paper'):
					print("THE COMPUTER WINS")
				if(computerChoice == 'rock' and userInput == 'rock'):
					print("DRAW")
				if(computerChoice == 'paper' and userInput == 'paper'):
					print("DRAW")
				if(computerChoice == 'scissors' and userInput == 'scissors'):
					print("DRAW")
	newFile.close()
	
rockCount, paperCount, scissorsCount = analysis("logFile.txt")
gameFunction("logFile.txt", rockCount, paperCount, scissorsCount)
