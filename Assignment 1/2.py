'''
A light ray is incident from medium-1 to medium-2. If the refractive indices of
medium-1 and medium-2 are 1.5 and 1.36 respectively then determine the angle of
refraction for an angle of incidence of .
'''
import math

n1 = 1.5
n2 = 1.36 

angle_incident = float(input("Enter the value for Incidence (degree): "))

critical_angle = math.asin(n2/n1)

if critical_angle<(angle_incident*3.14/180):

	print('The Ray would get Refracted Back To medium-1')
else:
	print("The Angle of Refraction (Radian) : ", math.asin(n1*math.sin(angle_incident*3.14/180)/n2))
