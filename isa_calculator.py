#import sys
import math

g = 9.80665
R = 287.00
def cal(p0, t0, a, h0, h1):
	if a != 0:
		t1 = t0 + a * (h1 - h0)
		p1 = p0 * (t1 / t0) ** (-g / a / R)
	else:
		t1 = t0
		p1 = p0 * math.exp(-g / R / t0 * (h1 - h0))
	return t1, p1

def isa(altitude):
	a = [-0.0065, 0, 0.0010, 0.0028, 0, -0.0028, -0.0020]
	h = [11000, 20000, 32000, 47000, 51000, 71000, 85000]
	p0 = 101325
	t0 = 288.15
	prevh = 0
	if altitude < 0 or altitude > 85000:
		print("You are in space!!Go back or you will die!!Altitude must be in [0, 85000]")
		return
	for i in range(0, 7):
		if altitude <= h[i]:
			temperature, pressure = cal(p0, t0, a[i], prevh, altitude)
			break;
		else:
			# sth like dynamic programming
			t0, p0 = cal(p0, t0, a[i], prevh, h[i])
			prevh = h[i]

	density = pressure / (R * temperature)
	strformat = 'Temperature: {0:.4f} k \nPressure: {1:.4f} Pa \nDensity: {2:.5f} kg/m3'
	print(strformat.format(temperature, pressure, density))
	
var = float(input("Please enter the altitude: ")) # the input gives a string so we need to use float to convert the string to number so isa can work
if var < 12000 and var > 0:
  print('This is the Troposphere. Your quantities are:')
elif var >= 12000 and var < 50000:
  print('This the Stratophere. Your quantities are:') 
elif var >= 50000 and var < 80000:
  print('This the Mesosphere. Your quantities are:')
elif var >= 80000 and var <= 85000:
  print('Congratulations!! You have reached the menopause.')
isa(var) # finally this gives the temperature,pressure and density at the altitude you inputed
