def Pizza(TotalPrice, Radius):
	pi = 3.1415926535897932384626433832795
	singleSlice = (2 * pi * Radius) / TotalPrice 
	finalCost = format(singleSlice, '.2f')
	return finalCost