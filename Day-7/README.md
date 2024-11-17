# Day-7
# Python Lists: An Introduction

## Overview

A **list** in Python is an ordered collection of items, which can be of any data type. Lists allow you to store multiple items in a single variable and access them using an index.

## Key Concepts

### 1. What is a List?
A list is a data structure that holds an ordered collection of items. These items can be numbers, strings, or other data types.

# creating a list
```python
# You can create a list by enclosing elements in square brackets [ ].
my_list = [1, 2, 3, 4, 5]
```
# Accessing List Elements
``` python
#List elements can be accessed using their index. Indexing starts at 0.
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 4
```
# List Indexing
``` python
#You can use both positive and negative indices to access elements from the list.

#Positive indexing starts from 0 (left to right).

#Negative indexing starts from -1 (right to left). 
print(my_list[-1])  # Output: 5
print(my_list[-2])  # Output: 4
```

#Adding Items to a List (Using append())
``` python
#To add a new item to the end of a list, you can use the append() method.
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```
# Task1:- Create a List of Favorite Foods and Print Each Item Using a Loop

In this task, we will create a list of favorite foods and print each item using a `for` loop.

### Expected output 
 Pizza

 Sushi
 
 Burger 
 
 Pasta
 
 Ice Cream


# Task 2: Create a List of Favorite Foods and Print Each Item Using a Loop

- We will add a new food item to the list.
- Then, we will print the updated list.
### Expected output
Updated List of Favorite Foods:

Pizza

Sushi

Burger

Pasta

Ice Cream

Tacos



