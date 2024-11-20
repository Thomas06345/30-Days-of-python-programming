'''Author:Thomas Cherian
   date: 20-11-24
   python program:A program that ask the users name until it is stoped using while'''
while True:
	user_input=input("Enter your name or enter exit to stop: ")
	if user_input=="exit":
		print("program ended")
		break
	else:
			print(f"Hi,your name is {user_input}")
			