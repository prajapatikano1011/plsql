# Practical 29: Remove None or empty values from a list

raw_list = ["apple", "", None, "banana", 0, False, [], "cherry", None]

# Filter out None and empty strings/containers (note: keeping valid 0/False if needed, or removing falsy)
cleaned = [x for x in raw_list if x is not None and x != ""]

print("Original list:", raw_list)
print("Cleaned list:", cleaned)
