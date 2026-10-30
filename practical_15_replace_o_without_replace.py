text = input("Enter string: ")

result = ""
for ch in text:
    if ch == 'o':
        result += '@'
    elif ch == 'O':
        result += '@'
    else:
        result += ch

print("Original string:", text)
print("Copied string:", result)
