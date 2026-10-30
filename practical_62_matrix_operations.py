# Practical 62: Matrix operations using nested lists

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

rows = len(matrix1)
cols = len(matrix1[0])

# 1. Matrix Addition
addition = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    addition.append(row)

# 2. Matrix Transpose (matrix1)
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix1[i][j])
    transpose.append(row)

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("\n1. Addition Result:")
for r in addition:
    print(r)

print("\n2. Transpose of Matrix 1:")
for r in transpose:
    print(r)

# 3. Sum of each row (matrix1)
print("\n3. Sum of each row (Matrix 1):")
for i in range(rows):
    print(f"Row {i + 1} sum: {sum(matrix1[i])}")

# 4. Sum of each column (matrix1)
print("\n4. Sum of each column (Matrix 1):")
for j in range(cols):
    col_sum = sum(matrix1[i][j] for i in range(rows))
    print(f"Column {j + 1} sum: {col_sum}")
