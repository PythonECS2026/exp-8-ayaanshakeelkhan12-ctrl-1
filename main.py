# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder: Khan Ayaan Shakeel
# Date:4/2/26


# Write your code here
# Triangle Pattern in Python

rows=int(input())

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
