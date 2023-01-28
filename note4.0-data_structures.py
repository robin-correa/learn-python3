# Important: Everything in python is an object

# [Lists]

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)  # [0, 0, 0, 0, 0, 'a', 'b', 'c']

numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)

# [Ascessing Items]
letters = ["a", "b", "c", "d"]
print(letters[-1])  # d
letters[0] = "A"
print(letters)  # ['A', 'b', 'c', 'd']
numbers = list(range(20))
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] / even numbers
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] / reverse order
print(numbers[::-1])

# [List unpacking]
numbers = [1, 2, 3, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(second)  # to get succeeding items

# [Looping over Lists]
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):  # (0, 'a'), (1, 'b')
    print(index, letter)

# [Adding or Removing Items]
letters = ["a", "b", "c"]
# Add
letters.append("d")
letters.insert(0, "-")  # inserts at the beginning of the items
print(letters)  # ['-', 'a', 'b', 'c', 'd']

# Remove
letters.pop()  # Removes the last item
print(letters)  # ['-', 'a', 'b', 'c']

# Remove with index
letters.pop(0)  # Removes the last item
print(letters)  # ['a', 'b', 'c']

# Remove with value
letters.remove("b")
print(letters)  # ['a', 'c']

# Delete items by index range
del letters[0:3]  # empty
print(letters)

letters.clear()  # delete all
print(letters)

# [Finding Items]
letters = ["a", "b", "c", "d"]
print(letters.count("d"))  # count: 1
if "d" in letters:
    print(letters.index("d"))  # index: 3
