'''Author:Thomas Cherian
   date: 8-11-24
   python program:To create a multipication table of given number up to 10.'''
num=int(input("Enter your number:"))
product=0
for i in range(1,11 ):
	product=num*i
	print(f"{num}×{i}={product}")