'''
Calculate the numerical aperture and acceptance angle for a fiber cable of
which and . The launching takes place from air.
'''
import math 
import cmath

print('Question  1')
print('Press 1 if Light cross Fiber via Axis ie. Meridional')
print('Press 2 if Light follow Helix path ie. Skew')
val = int(input("Enter your value: "))

if val==1:
	
	n1 = float(input("Enter the value for n1: "))
	n2 = float(input("Enter the value for n2: "))

	NA = math.sqrt((n1*n1) - (n2*n2))
	Acceptance_angle = math.asin(NA)
	print('The Numerical Aperture is: ',NA)
	print('The MAX Acceptance_angle is: ',Acceptance_angle,' radian')

elif val==2:
	n1 = float(input("Enter the value for n1: "))
	n2 = float(input("Enter the value for n2: "))
	alpha = float(input("Enter the value for alpha (Degree): "))

	NA = math.sqrt((n1*n1) - (n2*n2))
	Acceptance_angle = math.asin(NA/math.cos(alpha* 3.14 / 180))

	print('The Numerical Aperture is: ',NA)
	print('The MAX Acceptance_angle is: ',Acceptance_angle,' radian')


else:
	print('Wrong Input')