# Day 6: Functions in Python

## Objective

Learn how to define and use functions in Python to make code more reusable and organized.

## Topics

- What are functions?
- Defining functions with `def`
- Parameters and return values

## Key Concepts

### 1. Reusability of Code
Functions allow us to write code once and reuse it multiple times, reducing redundancy and making the code easier to manage.

### 2. Function Arguments and Return Values
- **Arguments**: Functions can accept inputs, called parameters, to perform tasks.
- **Return Values**: Functions can return values that can be used elsewhere in the program.

## What Are Functions?

A function is a block of reusable code that performs a specific task. Functions help break programs into smaller, manageable parts.
``` python
# Example 1: Simple Function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

#Example 2: Function with Return Value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

#Example 3: Function with Default Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")        # Output: Hello, Alice!
greet("Bob", "Hi")    # Output: Hi, Bob!
```

## Task-1:- Write a simple function that adds two numbers and returns the result.
## Task-2:- Write a function that checks if a number is positive, negative, or zero.

### Key Points:
- **add_numbers**: Adds two numbers and returns the result.
- **check_number**: Checks if a number is positive, negative, or zero and returns the corresponding string.













