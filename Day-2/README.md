# Day 2 - Check for Positive, Negative, or Zero

In this program, we will check whether a given number is positive, negative, or zero.

## Python Code:

```python
# Asking the user to input a number
num = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example:
# Input: -5
# Output: The number is negative.

# Input: 0
# Output: The number is zero.

# Input: 10
# Output: The number is positive.
