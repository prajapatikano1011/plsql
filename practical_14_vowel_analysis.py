text = input("Enter a string: ")
lower_text = text.lower()

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counts = {v: lower_text.count(v) for v in vowels}
total_vowels = sum(vowel_counts.values())

if total_vowels > 0:
    print("Vowels are present.")
    for v in vowels:
        print(f"Count of '{v}': {vowel_counts[v]}")
    print("Total number of vowels:", total_vowels)
else:
    print("No vowels found in the string.")
