text = 'I like "Python Programming" very much\nIt is my favorite subject'
ch = input("Enter a character to search: ")

if ch in text:
    print(f"Using 'in': '{ch}' is present in the string.")
else:
    print(f"Using 'in': '{ch}' is not present in the string.")

if ch not in text:
    print(f"Using 'not in': '{ch}' is absent in the string.")
else:
    print(f"Using 'not in': '{ch}' is present in the string.")
