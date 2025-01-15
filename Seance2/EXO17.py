numbers = []
shoe_sizes = []

for number in [1, 2, 3, 4, 5]:
    numbers.append(number)

for shoe_size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(shoe_size)

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

numbers.append(6)
numbers.append(6)
print("Number list with new values:",numbers)
numbers = list(set(numbers))
numbers.sort()
print("Numbers List without duplicates:", numbers)

additional_sizes = [13, 14]
for size in additional_sizes:
    shoe_sizes.append(size)
print("Updated Shoe Sizes List:", shoe_sizes)

combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)