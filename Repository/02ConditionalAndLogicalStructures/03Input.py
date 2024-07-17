"""
input() function - function for receive data from user

"""

print("what's your name?")
name = input()
print(f"good name {name}")

years = input("how old are you? ")
if years:
    age = int(years)
    if age < 18:
        print("omg, you're so young 👶")
        print(f"so, your name is {name} and you're {years} years old 👶")
    elif age < 60:
        print("omg, you look great 🧑‍")
        print(f"so, your name is {name} and you're {years} years old 🧑")
    else:
        print("omg you're so old 💀")
        print(f"oh, sorry, you...seem...well, so, your name is {name} and you're {years} years old 💀")
