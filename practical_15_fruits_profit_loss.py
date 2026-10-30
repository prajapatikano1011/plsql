fruits = {}

for i in range(6):
    name = input(f"Enter name of fruit {i+1}: ").strip()
    buy_price = float(input(f"Enter buying price of {name}: "))
    sell_price = float(input(f"Enter selling price of {name}: "))
    fruits[name] = (buy_price, sell_price)

profit_fruits = []
loss_fruits = []
break_even_fruits = []

for fruit, (buy, sell) in fruits.items():
    if buy < sell:
        profit_fruits.append(fruit)
    elif buy > sell:
        loss_fruits.append(fruit)
    else:
        break_even_fruits.append(fruit)

print("
Buying price less than selling price (Profit):", profit_fruits)
print("Buying price more than selling price (Loss):", loss_fruits)
print("No profit no loss:", break_even_fruits)
