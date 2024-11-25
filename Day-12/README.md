# Day 12: Introduction to Tuples

## Objective:
Learn what tuples are, how to create them, and how to use them.

## Topics:
- What is a tuple?
- Creating and accessing tuples
- The difference between tuples and lists
- Tuples are immutable, meaning they cannot be changed after creation.

## Key Concepts:
- Tuples are like lists but are immutable. Once created, you cannot modify the elements.
- Tuples are often used for storing related data that shouldn’t change, such as coordinates or RGB color values.

``` python
 Create a Tuple:
   hobbies = ("reading", "swimming", "coding")
print(hobbies)  # Output: ('reading', 'swimming', 'coding')

Accessing Tuple Elements:
   info = ('John', 25, 'New York')
name = info[0]
city = info[2]
print(name)  # Output: 'John'
print(city)  # Output: 'New York'

Tuple Unpacking:
 person = ('Alice', 'Smith', 30)
first_name, last_name, age = person
print(first_name)  # Output: 'Alice'
print(last_name)   # Output: 'Smith'
print(age)         # Output: 30


   
```
# Task 1:- Create a tuple of 3 items (e.g., your favorite colors or numbers) and print it.
# Task 2:- Create a tuple with a few items (e.g., a person's name, age, and city), and access and print each item using indexing.
# Task 3:- Create a tuple with 3 values (e.g., a person’s first name, last name, and age), and unpack the values into individual variables and print them.


## Notes:
- Tuples are immutable, which means their values cannot be changed once they are created. This makes them useful when you want to ensure that data remains constant.
- Tuples can be used in situations where the data will not be changed, such as storing coordinates, RGB values, or database records.
- Unlike lists, tuples use parentheses `()` instead of square brackets `[]`.
