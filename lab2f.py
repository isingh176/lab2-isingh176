#!/usr/bin/env python3

# Author: Ishwinder Singh
# Author ID: isingh176
# Date Created: 2004/05/19

import sys

# Assign the first command line argument to timer, converting it to an integer
timer = int(sys.argv[1])

# While loop to countdown until timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message
print("blast off!")

