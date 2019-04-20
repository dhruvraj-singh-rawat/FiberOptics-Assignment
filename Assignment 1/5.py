'''
Consider an optical link in which power at the transmitter is 0.1 mW and the
minimum power required at the receiver is 0.08 mW. The signal is transmitted
over the 1550 nm wavelength. What is the maximum length of the optical link,
assuming that there are no amplifiers? Assume an attenuation constant of
0.2dB/km.

'''
import math

input_db = 10*math.log10( 0.1 )
output_db = 10*math.log10( 0.08 )
attenuation_constant = 0.2

L =(input_db - output_db ) / attenuation_constant

print ( 'The maximum length of the Fiber is: ~',L)