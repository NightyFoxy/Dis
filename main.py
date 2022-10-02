import math
a = float(input("введите а\n"))
b = float(input("введите b\n"))
c = float(input("введите c\n"))
D = b**2 - 4*a*c
print ("Дискриминант", D)
if D>0:
	x1 = (-b + math.sqrt(D)) / 2*a
	x2 = (-b - math.sqrt(D)) / 2*a
	print (x1,x2)
elif D == 0:
	x1 = (-b)/ 2*a
	print (x1)
else:
	print ("Нет корней")