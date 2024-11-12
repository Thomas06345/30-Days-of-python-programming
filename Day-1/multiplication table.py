'''
Author:Vismaya Theresa Benny
Date:8/10/2024
python program to print multiplication table of a number upto 10
'''
Number=int(input("Enter a number:"))
for i in range(1,11):
    table=i*Number
    print(f"{i}*{Number} = {table}")