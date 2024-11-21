# Day 11: Conditionals (if-else Statements)

## Objective:
Learn how to make decisions in your code using if statements.

### Topics:
- Writing `if`, `elif`, and `else` statements
- Comparing values with `==`, `!=`, `<`, `>`, `<=`, `>=`, etc.

### Key Concepts:
Making decisions based on conditions.

---
```python
# Example 1:- Program to check if a number is divisible by both 3 and 5
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
# output
Enter a number: 15
15 is divisible by both 3 and 5.

# Example 2 :- # Program to check if a number is within a range
number = int(input("Enter a number: "))
if 10 <= number <= 20:
    print(f"{number} is between 10 and 20.")
else:
    print(f"{number} is not between 10 and 20.")
# output
Enter a number: 15
15 is between 10 and 20.
```
# Task 1:- Write a program that checks if a number is even or odd

# Task 2:- Write a program that checks if the user's input is greater than 10 or not.



