# Practical 35: Filter out all vowels from a list of characters

chars = ['a', 'b', 'c', 'e', 'g', 'i', 'k', 'o', 'p', 'u', 'z']
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

consonants = [c for c in chars if c not in vowels]

print("Character list:", chars)
print("After filtering vowels:", consonants)
