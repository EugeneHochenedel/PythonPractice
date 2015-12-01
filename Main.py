from Time import *
from Money import *
def Main():
	Prompt = input("Enter a number of seconds: ")
	X = int(Prompt)
	Y = hours(X)
	print(Y, "Hour(s)")
	Z = minutes(X)
	print(Z, "Minute(s)")
	A = seconds(X)
	print(A, "Second(s)")
	
	Prompt2 = input("Enter a number of pennies: ")
	M = int(Prompt2)
	N = Quarter(M)
	O = Dime(M)
	P = Nickle(M)
	print(N, "Quarters")
	print(O, "Dimes")
	print(P, "Nickels")
	print(M, "Pennies")
Main()