'''Author:Thomas Cherian
   date: 10-11-24
   python program:To find the which quadrant x and y lie.'''
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
if x>0 and y>0:
	print("First Quadrant ")
if x<0 and y>0:
	print("Second Quadrant ")
if x<0 and y<0:
	print("Third Quadrant ")
if x>0 and y<0:
	print("Fourth Quadrant ")