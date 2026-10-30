# Practical 27: Check if a list is a palindrome

words = ["radar", "hello", "level", "world"]

def check_palindrome(lst):
    return lst == lst[::-1]

test1 = [1, 2, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]

print("Test 1:", test1, "-> Palindrome?", check_palindrome(test1))
print("Test 2:", test2, "-> Palindrome?", check_palindrome(test2))
