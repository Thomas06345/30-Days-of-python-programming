'''Author:Thomas Cherian
   date: 14-11-24
   python program:To check whether the given.string is palindrome or not .'''
word=input("Enter a word to be checked:") 
if word[0: ]==word[: :-1] :
	print(f"The given word {word} is palindrome")
else:
		print(f"The given word {word} is not palindrome")