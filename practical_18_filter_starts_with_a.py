names = ["Amit", "Rohit", "Ananya", "Suresh", "Aarav", "Pooja"]
a_names = list(filter(lambda name: name.startswith("A") or name.startswith("a"), names))
print(a_names)
