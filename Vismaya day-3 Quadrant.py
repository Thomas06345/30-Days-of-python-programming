x=int(input("Enter the X value:"))
y=int(input("Enter the y value:"))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
else:
    print("Quadrant 4")