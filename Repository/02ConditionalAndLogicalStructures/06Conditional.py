"""
conditional control commands
if, elif and else

"""

x = input("what's the value of x? ")
y = input("what's the value of y? ")

if y > x:
    print("y is greater than x")
elif x > y:
    print("x is greater than y")
else:
    print("x equals y")

print("code outside conditional block")
#te