"""
repetition structures - loops

while

"""

# first example
a = 0

while a <= 5:
    print(a)
    print(a <= 5)
    if a == 3:
        break
    a = a + 1

print("final result: ", a)
print(a <= 5)

# second example
while a <= 5:
    print(a)
    print(a <= 5)
    a = a + 1
else:
    print(f"is not less than or equal to 5. value of {a}")

