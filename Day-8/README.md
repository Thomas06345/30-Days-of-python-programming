# Day-8:- Python List Operations 

## Objective:
Learn more operations on lists, including removing items, sorting, and slicing.

## Key Concepts:
- **Modifying Lists**: Using methods like `remove()` and `pop()` to modify lists.
- **Slicing**: Extracting parts of a list using slicing syntax.

### Examples:

#### Example 1: : **Modifying a List (Removing a specific item)**

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Remove a specific item using remove()
fruits.remove("banana")
print("List after removing 'banana':", fruits) #Output:-["apple", "cherry", "date", "elderberry"].
```
#### Example 2: Slicing a List (Print even numbers)
```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list slicing to print even numbers (every second item starting from index 1)
even_numbers = numbers[1::2]
print("Even numbers:", even_numbers) #Output:- [2, 4, 6, 8, 10].
```
## Exercise:

1. **Remove the last item from a list.**
   
2. **Create a list of numbers and print the even numbers using list slicing.**

---








