'''
Find the approximate number of modes for a signal operating at 850 nm in 
a step-index fiber with a 100 µm core. Assume that the refractive index 
of glass in the core is 1.5 and the refractive index of the cladding is 
1.47.
'''
import math

n1=1.5
n2= 1.47
NA = math.sqrt((n1*n1) - (n2*n2))

alpha = 100 * (10 ** -6)
lamda = 850 * (10 ** -9)

V = (2 * 3.14 * alpha * NA ) / lamda
Modes = int ((V ** 2) / 2)
print ('The Number of Modes : '~,Modes)
