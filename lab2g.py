#!/usr/bin/env python3

# Author: Ishwinder Singh
# Author ID: isingh176
# Date Created: 2024/09/21
import sys

# Check if argument is provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Set timer to the argument
else:
    timer = 3  # Default timer value

# Loop until the timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrease the timer by 1 each time

# Print "blast off!" when the loop ends
print("blast off!")
