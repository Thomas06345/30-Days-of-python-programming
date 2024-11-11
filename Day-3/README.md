# Day 3 - Temperature Range

In this program, we will read the temperature from the user and determine whether it's "Freezing", "Cold", "Warm", or "Hot" based on the value provided.

## Python Code:

```python
# Asking the user to input the temperature
temperature = float(input("Enter the temperature in Celsius: "))

# Determining the temperature range
if temperature < 0:
    print("Freezing")
elif 0 <= temperature <= 15:
    print("Cold")
elif 16 <= temperature <= 30:
    print("Warm")
else:
    print("Hot")

# Example:
# Input: -5
# Output: Freezing

# Input: 10
# Output: Cold

# Input: 25
# Output: Warm

# Input: 35
# Output: Hot
