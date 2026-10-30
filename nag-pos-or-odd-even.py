nums=[45,56,78,23,40,11,99,100,-12,-45,0]
pos=[n for n in nums if n > 0]
nag=[n for n in nums if n < 0]
odd=[n for n in nums if n%2 == 1]
even=[n for n in nums if n%2 == 0]
squares=[n**2 for n in nums]
print("positive numbers:",pos)
print("nagative numbers:",nag)
print("odd numbers:",odd)
print("even numbers:",even)
print("squaresn:",squares)
