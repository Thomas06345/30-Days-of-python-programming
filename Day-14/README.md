# Day 14: Dictionaries (Introduction)

## Objective:
Understand how dictionaries work in Python.

## Topics:
- What are dictionaries?
- Creating and accessing dictionaries
- Keys and values

## Key Concepts:

### What are Dictionaries?
A dictionary in Python is an unordered collection of items. Each item is stored as a pair of key and value. Dictionaries allow you to store data in key-value pairs, where each key is unique, and it maps to a corresponding value.

### Storing data as key-value pairs:
A dictionary in Python is defined using curly braces `{}` with the keys and values separated by a colon `:`. Each key-value pair is separated by commas.

### Creating a Dictionary:
A dictionary is created using curly braces, with the key-value pairs defined as follows:

```python
# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
```
### Accessing Dictionary Values:

You can access values in a dictionary using their corresponding keys:
``` python
# Accessing dictionary values
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
```
### Adding or Updating Values:

You can add or update key-value pairs in a dictionary:
``` python
# Adding a new key-value pair
person["favorite_color"] = "blue"
```
Removing Items:

You can remove an item from a dictionary using the del keyword:
``` python
# Removing a key-value pair
del person["age"]
```
# Task 1:- Create a dictionary with your name, age, and city. Print each value.
# Task 2:- Add a new key-value pair to your dictionary (e.g., "favorite_color": "blue").

















