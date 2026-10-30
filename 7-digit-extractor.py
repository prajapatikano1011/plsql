num=float(input("enter 3 digit number:"))

hundreds=num // 100
tens = (num // 10) % 10
units = num % 10 

sum_digit=hundreds+tens+units
product_digit=hundreds*tens*units

print(f"hundreds digit: {hundreds:.2f}")
print(f"tens digit: {tens:.2f}")
print(f"unints digit: {units:.2f}")
print(f"sum of digit: {sum_digit:.2f}")
print(f"product digit: {product_digit:.2f}")