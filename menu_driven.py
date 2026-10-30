x = input("enter string: ")

print("1. find length")
print("2. upper case")
print("3. lower case")
print("4. initial capital")
print("5. split string")

y = int(input("enter choice(1-5): "))

if y == 1:
    print(len(x))
elif y == 2:
    print(x.upper())
elif y == 3:
    print(x.lower())
elif y == 4:
    print(x.capitalize())
elif y == 5:
    print(x.split())
else:
    print("in valid choice")