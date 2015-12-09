import math
from math import *
class Scalars(object):
	def __init__(self, x):
		self.x = x
	def value(self):
		print(self.x, '\n')
	def __add__(self, addScal):
		overAdd1 = Scalars(0)
		overAdd1.x = self.x + addScal.x
		return overAdd1.value()
	def __sub__(self, subScal):
		overSub1 = Scalars(0)
		overSub1.x = self.x - subScal.x
		return overSub1.value()
	
	def __mul__(self, multiScal):
		overMulti1 = Scalars(0)
		overMulti1.x = self.x * multiScal.x
		return overMulti1.value()

	def LinearInterpolation(self, secondScal, inbetween):
		onLine1 = Scalars(0)
		onLine1.x = self.x + inbetween * (secondScal.x - self.x)
		return onLine1.value()


class Vectors2D(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def value(self):
		print(self.x,",",self.y, '\n')
	def __add__(self, addVec):
		overAdd2 = Vectors2D(0, 0)
		overAdd2.x = self.x + addVec.x
		overAdd2.y = self.y + addVec.y
		return overAdd2.value()
	def __sub__(self, subVec):
		overSub2 = Vectors2D(0, 0)
		overSub2.x = self.x - subVec.x
		overSub2.y = self.y - subVec.y
		return overSub2.value()
	def __mul__(self, multiVec):
		overMulti2 = Vectors2D(0, 0)
		overMulti2.x = self.x * multiVec.x
		overMulti2.y = self.y * multiVec.y
		return overMulti2.value()
	def LinearInterpolation2D(self, secondPoint, inbetween):
		Linear2 = Vectors2D(0, 0)
		Linear2.x = self.x + inbetween * (secondPoint.x - self.x)
		Linear2.y = self.y + inbetween * (secondPoint.y - self.y)
		return Linear2.value()
	def Magnitude2D(self):
		squared2 = Vectors2D(0, 0)
		squared2.x = self.x * self.x
		squared2.y = self.y * self.y
		root2 = math.sqrt(squared2.x + squared2.y)
		return root2
	def Normalizing2D(self):
		norm2 = Vectors2D(0, 0)
		normRoot2 = self.Magnitude2D()
		norm2.x = self.x / normRoot2
		norm2.y = self.y / normRoot2
		return norm2.value()
	def DotProduct2D(self, vecTwo):
		dot2 = Vectors2D(0, 0)
		dot2.x = (self.x * vecTwo.x)
		dot2.y = (self.y * vecTwo.y)
		dot2D = dot2.x + dot2.y 
		return dot2D
		
		
class Vectors3D(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def value(self):
		print(self.x,",",self.y,",", self.z, '\n')
	def __add__(self, addVec):
		overAdd3 = Vectors3D(0, 0, 0)
		overAdd3.x = self.x + addVec.x
		overAdd3.y = self.y + addVec.y
		overAdd3.z = self.z + addVec.z
		return overAdd3.value()
	def __sub__(self, subVec):
		overSub3 = Vectors3D(0, 0, 0)
		overSub3.x = self.x - subVec.x
		overSub3.y = self.y - subVec.y
		overSub3.z = self.z - subVec.z
		return overSub3.value()
	def __mul__(self, multiVec):
		overMulti3 = Vectors3D(0, 0, 0)
		overMulti3.x = self.x * multiVec.x
		overMulti3.y = self.y * multiVec.y
		overMulti3.z = self.z * multiVec.z
		return overMulti3.value()
	def LinearInterpolation3D(self, secondPoint, inbetween):
		Linear3 = Vectors3D(0, 0, 0)
		Linear3.x = self.x + inbetween * (secondPoint.x - self.x)
		Linear3.y = self.y + inbetween * (secondPoint.y - self.y)
		Linear3.z = self.z + inbetween * (secondPoint.z - self.z)
		return Linear3.value()
	def Magnitude3D(self):
		squared3 = Vectors3D(0, 0, 0)
		squared3.x = self.x * self.x
		squared3.y = self.y * self.y
		squared3.z = self.z * self.z
		root3 = math.sqrt(squared3.x + squared3.y + squared3.z)
		return root3
	def Normalizing3D(self):
		norm3 = Vectors3D(0, 0, 0)
		normRoot3 = self.Magnitude3D()
		norm3.x = self.x / normRoot3
		norm3.y = self.y / normRoot3
		norm3.z = self.z / normRoot3
		return norm3.value()
	def DotProduct3D(self, vecThree):
		dot3 = Vectors3D(0, 0, 0)
		dot3.x = (self.x * vecThree.x)
		dot3.y = (self.y * vecThree.y)
		dot3.z = (self.z * vecThree.z)
		dot3D = dot3.x + dot3.y + dot3.z
		return dot3D

class Vectors4D(object):
	def __init__(self, x, y, z, a):
		self.x = x
		self.y = y
		self.z = z
		self.a = a
	def value(self):
		print(self.x,",",self.y,",", self.z,",",self.a, '\n')
	def Magnitude4D(self):
		squared4 = Vectors4D(0, 0, 0, 0)
		squared4.x = self.x * self.x
		squared4.y = self.y * self.y
		squared4.z = self.z * self.z
		squared4.a = self.a * self.a
		root4 = math.sqrt(squared4.x + squared4.y + squared4.z + squared4.a)
		return root4
	def Normalizing4D(self):
		norm4 = Vectors4D(0, 0, 0, 0)
		normRoot4 = self.Magnitude4D()
		norm4.x = self.x / normRoot4
		norm4.y = self.y / normRoot4
		norm4.z = self.z / normRoot4
		norm4.a = self.a / normRoot4
		return norm4.value()
		
	
def HexCode(astring):
	ColorValues = Vectors4D(0, 0, 0, 0)
	if astring[0] == '#':
		HexRay[6]
		for values in HexRay:
			first = 1
			first <= 6
			first+=1
			HexRay[first - 1] = astring[first]

		for values in HexRay:
			second = 0
			second < 6
			second+=1
			if HexRay[second] / 10 == 4 or HexRay[second] / 10 == 5:
				HexRay[second] = HexRay[second] - 48
			elif HexRay[second] / 10 == 6 or HexRay[second] / 10 == 7:
				HexRay[second] = HexRay[second] - 55
			else:
				HexRay[second] = HexRay[second]

		ColorValues.x = (HexRay[0] * 16) + HexRay[1]
		ColorValues.y = (HexRay[2] * 16) + HexRay[3]
		ColorValues.z = (HexRay[4] * 16) + HexRay[5]
		ColorValues.a = 255
		return ColorValues.value()

	else:
		ColorValues.x = 0
		ColorValues.y = 0
		ColorValues.z = 0
		ColorValues.a = 0
		return ColorValues.value()