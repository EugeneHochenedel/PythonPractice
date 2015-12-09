from MathLibrary import *
def Main():
	scalar1 = Scalars(4)
	scalar2 = Scalars(8)
	vec2D1 = Vectors2D(4, 6)
	vec2D2 = Vectors2D(5, 7)
	vec3D1 = Vectors3D(2, 11, 16)
	vec3D2 = Vectors3D(-1, 8, 13)
	vec4D1 = Vectors4D(7, 5, 10, 9)
	str = ['#FF3366']
	
	print("Scalar addition:")
	scalar3 = scalar1 + scalar2
	
	print("Scalar subtraction:")
	scalar3 = scalar1 - scalar2
	
	print("Scalar multiplication")
	scalar3 = scalar1 * scalar2
	
	print("Scalar Linear Interpolation:")
	face = input("Input a value greater than 0 and less than 1: ")
	num = float(face)
	scalar3 = scalar1.LinearInterpolation(scalar2, num)
	
	print("2D Vector addition:")
	vec2D3 = vec2D1 + vec2D2
	
	print("2D Vector subtraction:")
	vec2D3 = vec2D1 - vec2D2
	
	print("2D Vector multiplication:")
	vec2D3 = vec2D1 * vec2D2
	
	print("2D Vector Linear Interpolation:")
	face = input("Input a value greater than 0 and less than 1: ")
	num = float(face)
	vec2D3 = vec2D1.LinearInterpolation2D(vec2D2, num)
	
	vec2D3 = vec2D1.Magnitude2D()
	print("2D Vector Magnitude:\n", vec2D3, '\n')
	
	print("2D Vector Normalization:")
	vec2D3 = vec2D1.Normalizing2D()
	
	vec2D3 = vec2D1.DotProduct2D(vec2D2)
	print("2D Dot Product:\n", vec2D3, '\n')
	
	print("3D Vector addition:")
	vec3D3 = vec3D1 + vec3D2
	
	print("3D Vector subtraction:")
	vec3D3 = vec3D1 - vec3D2
	
	print("3D Vector multiplication:")
	vec3D3 = vec3D1 * vec3D2
	
	print("3D Vector Linear Interpolation:")
	face = input("Input a value greater than 0 and less than 1: ")
	num = float(face)
	vec3D3 = vec3D1.LinearInterpolation3D(vec3D2, num)
	
	vec3D3 = vec3D1.Magnitude3D()
	print("3D Vector Magnitude:\n", vec3D3, '\n')
	
	print("3D Vector Normalization:")
	vec3D3 = vec3D1.Normalizing3D()
	
	vec3D3 = vec3D1.DotProduct3D(vec3D2)
	print("3D Dot Product:\n", vec3D3)
	
	print("4D Vector Normalization:")
	vec4D2 = vec4D1.Normalizing4D()
	
	print("Constructing from Hexadecimals:")
	vec4D2 = HexCode('#FF3366')

Main()