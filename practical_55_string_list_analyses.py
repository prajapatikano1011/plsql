# Practical 55: List of strings analysis

words = ["elephant", "cat", "umbrella", "orange", "sky", "dog", "apple"]
print("Words:", words)

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

# Longest and Shortest
longest = max(words, key=len)
shortest = min(words, key=len)

# Starting with vowel
starts_vowel = [w for w in words if w.lower().startswith(vowels)]

# Ending with consonant (alphabet character not in vowels)
ends_consonant = [w for w in words if w[-1].isalpha() and w[-1].lower() not in vowels]

print("Longest string:", longest)
print("Shortest string:", shortest)
print("Strings starting with a vowel:", starts_vowel)
print("Strings ending with a consonant:", ends_consonant)
