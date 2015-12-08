from Cost import *
def Main():
	inFile = open("Names.txt", 'r')
	nameList = inFile.readlines()
	nameList.sort()
	for students in nameList:
		print(students)
	
	Cost = input("Enter the price of a pizza (in USD): $")
	Size = input("Enter the radius of a pizza (in inches): ")
	X = float(Cost)
	Y = float(Size)
	OnePiece = Pizza(X, Y)
	print("The price for one slice of that pizza will be: $", OnePiece)
Main()