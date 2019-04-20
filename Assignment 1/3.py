'''
Consider a step-index fiber has a core with refractive index 1.495. What is the 
maximum refractive index of the cladding in order for light entering the fiber
at an angle of 60 degrees to propagate through the fiber? Air has refractive 
index of 1.0.

'''

import math

index_core= 1.495
angle_incidence = 60

index_cladding = math.sqrt(index_core ** 2 - ( math.sin(3.14*angle_incidence/180) ** 2 ) ) 
print('The Refractive index of cladding should be : ',index_cladding)