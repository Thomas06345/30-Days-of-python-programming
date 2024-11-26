# Day 13: Introduction to Sets

## Objective:
Learn what sets are, how to create them, and how to perform basic operations with sets.

### Topics:
- What is a set?
- Creating and accessing sets
- Sets do not allow duplicate items, so they automatically remove duplicates
- Basic set operations: union, intersection, and difference

---

## Key Concepts:

### 1. **What is a Set?**
A set is a collection of unique elements. This means that sets automatically remove duplicates and only store one instance of each element. Sets are unordered, so the items do not have a specific order.

### 2. **Creating and Accessing Sets:**
You can create a set in Python by using curly braces `{}` or the `set()` function.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding duplicate item to set
my_set = {1, 2, 3, 4}
my_set.add(4)  # Adding duplicate element
print(my_set)  # Output will be {1, 2, 3, 4}, no duplicate element
```

## Basic Set Operations:
### 1. Union
The union of two sets returns a set containing all the elements from both sets, without duplicates.
``` python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Union of set1 and set2
print(union_set)  # Output will be {1, 2, 3, 4, 5}
```
### 2. Intersection
The intersection of two sets returns a set containing only the elements that are present in both sets.
``` python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # Intersection of set1 and set2
print(intersection_set)  # Output will be {3}
```
### 3. Difference
``` python
The difference of two sets returns a set containing elements that are in the first set but not in the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # Difference between set1 and set2
print(difference_set)  # Output will be {1, 2}
```
## Set membership
You can check if an element is part of a set using the in keyword:
``` python
fruit_set = {"apple", "banana", "cherry"}
# Checking if 'apple' is in the set
print("apple" in fruit_set)  # Output will be True

# Checking if 'orange' is in the set
print("orange" in fruit_set)  # Output will be False
```
# Task 1:- Create a set of your favorite fruits and print it. Add a duplicate fruit and print the set again to see that the duplicate is automatically removed.
# Task 2:- Create two sets: one with odd numbers and one with even numbers. Use set operations to find:

- The union of the two sets.

- The intersection (common elements) of the two sets.

- The difference (items in one set but not the other).

# Task 3:- Check if a specific fruit is in your set using the in keyword (e.g., check if "apple" is in the fruit set).









