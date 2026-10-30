words = ["cat", "dog", "tiger", "lion", "elephant", "bear"]
words_with_a = list(filter(lambda w: 'a' in w.lower(), words))
print(words_with_a)
