P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time (T in years): "))

SI = (P * R * T) / 100

total_amount = P + SI

print(f"Simple Interest (SI): {SI}")
print(f"Total Amount (P + SI): {total_amount}")