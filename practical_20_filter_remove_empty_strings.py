strings = ["hello", "", "world", "", "python", " ", "code"]
non_empty = list(filter(lambda s: s.strip() != "", strings))
print(non_empty)
