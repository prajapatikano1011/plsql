s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")

if s2 in s1:
    total_count = s1.count(s2)
    print(f"'{s2}' occurs {total_count} time(s) in s1.")
else:
    print("s2 is not present in s1.")
