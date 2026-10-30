# Practical 49: Sentence to words, count occurrences, remove repeated words

sentence = input("Enter a sentence: ")
words = sentence.split()

print("\nAll words:", words)

# Word frequency
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("\nWord Frequencies:")
for w, count in freq.items():
    print(f"'{w}': {count}")

# Unique words
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("\nWords after removing duplicates:")
print(unique_words)
