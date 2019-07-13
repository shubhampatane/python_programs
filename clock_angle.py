#Enter duration of day and longitude as input. Get Degree between hour hand and minute hand as output
# dur_day =12, longitude = 82.5 output: angle = 15 degree
import math
p = int(input())
l = float(input())
r = (p*l)/360
m,h = math.modf(r)

h = h%12
m= int(m*60)
ma = m*6
ha = h*30 + m*0.5
deg = abs(ha-ma)
if deg>180:
    deg = 360-deg
print("%.2f" % deg)
