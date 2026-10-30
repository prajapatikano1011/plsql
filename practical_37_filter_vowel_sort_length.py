words = ["apple", "cat", "umbrella", "dog", "elephant", "ox", "ice"]
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
vowel_words = sorted(filter(lambda w: w.startswith(vowels), words), key=lambda w: len(w))
print(vowel_words)
