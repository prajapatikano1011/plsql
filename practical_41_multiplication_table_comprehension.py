# Practical 41: Multiplication table (list of lists) using comprehension

table = [[i * j for j in range(1, 11)] for i in range(1, 6)]

print("Multiplication tables (1 to 5):")
for row_idx, row in enumerate(table, 1):
    print(f"Table of {row_idx}: {row}")
