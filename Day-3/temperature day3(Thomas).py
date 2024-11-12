'''Author:Thomas Cherian
   date: 10-11-24
   python program:To find weather using given temperature  .'''
temp=int(input("Enter temperature:"))
if temp<0:
	print("Freezing")
elif temp>0 and temp<=15:
	print("Cold")
elif temp>16 and temp<=30:
	print("Warm")
else:
	print("Hot")