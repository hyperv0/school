#What is the output of the following code
import math
a,b = bool(0), bool(0.0)
c,d = str(0), str(0.0)

#print(len(a), len(b)) 
print(len(c), len(d)) 

tp1 = (15,11,17,16,12)
#tp1.pop(12)
#print(tp1)

tp = (5,)
tp1 = tp * 2
print(len(tp1))

plane = ('passangers', 'luggage')
plane = list(plane)
plane[1] = 'Electronic Items'
print(plane)

t = (1, (2,3,4,5), (6,7,8), 9)
#print(sum(t))

a = 5
b = 10
r = 10

vol = 4/3*(math.pi)*pow(r,3)
print(vol)