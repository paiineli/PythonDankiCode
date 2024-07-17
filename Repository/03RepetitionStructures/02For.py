"""
repetition structures - loops

for

"""

# first example
s = "sorocaba"

for x in s:
    print(x)

# second example
for x in range(6):
    print(x)

# third example
for x in range(5, 8):
    print(x)

# fourth example
for x in range(0, 6, 2):  # range(6)
    print(x)

# fifth example
for x in range(6):  # for(x=0;x<=5;x++)
    print(x)
else:
    print("we've reached the end")
