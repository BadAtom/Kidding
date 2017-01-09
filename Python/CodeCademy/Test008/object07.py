from itertools import product, permutations

letters = "abc"

print(list(product(letters, range(5))))
print(list(permutations(letters)))
