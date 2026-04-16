# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder: Khan Ayaan Shakeel
# Date:4/2/26

print("--- Pattern Printer ---\n")

# Write your code here
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
