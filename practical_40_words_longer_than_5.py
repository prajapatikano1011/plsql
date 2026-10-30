# Practical 40: Extract words longer than 5 letters from a sentence

sentence = "Python programming language is versatile and popular for problem solving"
words = sentence.split()

long_words = [w for w in words if len(w) > 5]

print("Sentence:", sentence)
print("Words longer than 5 letters:", long_words)
