# Day 10: Loops - while Loop

## Objective:
Learn how to use the `while` loop for repeated tasks.

## Topics:
- What is a `while` loop?
- Creating `while` loops with conditions
- Stopping a loop with `break`

## Key Concepts:
- Repeating tasks based on a condition
- Using loops to automate repetitive tasks

---

## 1. What is a `while` loop?

A `while` loop is a control flow statement that allows code to be executed repeatedly based on a given condition. The loop continues as long as the condition is true. If the condition is false at the start, the loop body is not executed.

### Syntax:
```python
# Example 1
while condition:
    # code block to execute
i = 0
while i < 5:
    print(i)
    i += 1
# Output
0
1
2
3
4

# Example 2:- Breaking the Loop When User Types "exit"
while True:
    user_input = input("Enter a number (or type 'exit' to stop): ")
    if user_input == "exit":
        print("Exiting the program.")
        break
    else:
        print(f"You entered: {user_input}")
# Output
Enter a number (or type 'exit' to stop): 12
You entered: 12
Enter a number (or type 'exit' to stop): 7
You entered: 7
Enter a number (or type 'exit' to stop): exit
Exiting the program.
```
# Task 1:- Write a program that asks the user to enter their name repeatedly until they type "stop".
# Task 2:- Write a program that counts down from 5 to 0 using a while loop





