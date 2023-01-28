# [Swapping Variables]
from pprint import pprint
from array import array
x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)

# Technique (tutples):
x, y = y, x

# [Arrays]
numbers = array("i", [1, 2, 3])
numbers.append(4)

print(list(numbers))

# [Sets] - Does not support indexing

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
second.add(5)
# second.remove(5)
len(second)
print(second)  # {1, 4, 5}

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)  # {1, 2, 3, 4, 5}
print(first & second)  # {1}
print(first - second)  # {2, 3, 4}
print(first ^ second)  # {2, 3, 4, 5} - Removes duplicate in both sets (1)

if 1 in first:
    print("yes")

# [Dictionaries] - Collection of key/value pairs
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])

point["x"] = 10
point["z"] = 20

print(point)  # {'x': 10, 'y': 2, 'z': 20}

print(point.get("a", 0))  # If not exist, return 0

del point["x"]
print(point)  # {'y': 2, 'z': 20}

for key, value in point.items():
    print(key, value)


# [Dictionary Comprehensions]
# Formula [expression for item in items]

# Long method
values = []
for x in range(5):
    values.append(x * 2)

# Short method
values = [x * 2 for x in range(5)]

# [Unpacking Operator]
numbers = [1, 2, 3]
print(*numbers)  # Same as JS spread operator "..."

values = list(range(5))
values = [*range(5), *"Hello"]

print(values)  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

first = [1, 2]
second = [3]
values = [*first, "a", *second]

print(values)

dictionary1 = {"x": 1}
dictionary2 = {"x": 10, "y": 2}
combined = {**dictionary1, **dictionary2, "z": 1}

print(combined)  # {'x': 10, 'y': 2, 'z': 1}

# [Exercise] - Get the repeated characters for the sentence

sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
pprint(char_frequency_sorted)
