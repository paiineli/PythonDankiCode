"""
python exercises

observation: all exercises will use the “input” function,
so that the user can enter the data

1 area of a rectangle
2 area of a square
3 if the product you are evaluating costs (??) reais, what will it cost with a (??)% discount?
4 area of a circle
5 conversion from reals to dollars
6 dollar to real conversion

"""

# Exercise 1: Area of a Rectangle
print("Calculate the rectangle's area")
base = input("What's the rectangle's base? ")
height = input("What's the rectangle's height? ")
area = float(base) * float(height)
print(f"Your rectangle has an area of: {area}")

# Exercise 2: Area of a Square
print("Calculate the square's area")
side = input("What's the square's side length? ")
area = float(side) ** 2
print(f"Your square has an area of: {area}")

# Exercise 3: Product Discount
print("Calculate the discount for your product")
product_price = input("How much does your product cost? ")
discount = input("What is your discount percentage? ")
product_discount = float(product_price) * float(discount) / 100
discounted_price = float(product_price) - product_discount
print(f"The price of the discounted product is: {discounted_price}")

# Exercise 4: Area of a Circle
print("Calculate the circle's area")
radius = input("What's the circle's radius? ")
pi = 3.14159
area = pi * float(radius) ** 2
print(f"Your circle has an area of: {area}")

# Exercise 5: Conversion from BRL to US$
print("Conversion from BRL to US$")
dollar = input("How much is the dollar today? ")
brl = input("How many reals do you want to convert? ")
conversion = float(brl) / float(dollar)
print(f"The converted amount is: {conversion} US$")

# Exercise 6: Conversion from US$ to BRL
print("Conversion from US$ to BRL")
real = input("How much is the real today? ")
dollars = input("How many dollars do you want to convert? ")
conversion = float(dollars) * float(real)
print(f"The converted amount is: {conversion} BRL")


