# Practical 14: Convert a list of strings to a list of integers

str_list = ["10", "25", "30", "45", "50"]
print("String list:", str_list)

int_list = []
for s in str_list:
    int_list.append(int(s))

print("Integer list:", int_list)
