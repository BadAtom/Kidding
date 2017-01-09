bank = []

for num in range(10):
    bank.append("iteration" + str(num))

print('10' in bank)
print('iteration' in bank)
print('iteration' in bank[0])

def array_sublimer(array):
    list(array).reverse
    return array

print(bank)
array_sublimer(bank)
print(bank)

bank.append("iteration0")
print(bank)
bank.remove("iteration0")
print(bank)