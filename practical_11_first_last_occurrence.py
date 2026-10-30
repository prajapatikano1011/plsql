s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")

if s2 in s1:
    first_idx = s1.find(s2)
    last_idx = s1.rfind(s2)
    print("First occurrence at index:", first_idx)
    print("Last occurrence at index:", last_idx)
else:
    print("s2 is not found in s1.")
