'''Author:Thomas Cherian
   date: 14-11-24
   python program:To print a triangular pattern of stars .'''
number=int(input("Enter the range:"))
for i in range(1,number+1):
	for j in range(i):
		print("*",end=" ")
	print()