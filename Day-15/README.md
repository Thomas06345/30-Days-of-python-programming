# Day 15: Dictionaries (More Operations)

## Objective:
Learn how to modify dictionaries.

## Topics:
- Updating values in a dictionary
- Removing key-value pairs (`del`)
- Iterating over dictionary items
- Printing keys from a dictionary

## Key Concepts:
- Modifying and deleting items in dictionaries

---
```python
# Example 1: Updating values in a dictionary

You can update the value associated with a key in a dictionary by directly assigning a new value to the key.

# Define a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Update the age
person['age'] = 31

print(person) # {'name': 'John', 'age': 31, 'city': 'New York'}

# Example 2: Removing key-value pairs using del

You can delete key-value pairs from a dictionary using the del statement.

# Define a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Remove the 'city' key-value pair
del person['city']

print(person) # output {name': 'John', 'age': 30}

# Example 3: Printing keys from a dictionary

You can print only the keys of a dictionary by using the .keys() method.
 # Define a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Print only the keys
for key in person.keys():
    print(key)
# Output:

name
age
city
```
# Task 1-Write a program that updates the age in your dictionary.
# Task 2-Write a program that prints all the keys in your dictionary.
