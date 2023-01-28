# [Sorting Lists]

from collections import deque
numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# will not modify the existing list
print(sorted(numbers))
# will not modify the existing list - Reversed
print(sorted(numbers, reverse=True))
print(numbers)

# Sorting tuple of 3 items
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# [Lambda Functions]: key=lambda  <parameters:expression>
items.sort(key=lambda item: item[1])
print(items)

# [Map Function]

# Sorting tuple of 3 items
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# iterable / can't print or display yet
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# iterable / create list
prices = list(map(lambda item: item[1], items))
print(prices)

# [Filter Function]
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)  # [('Product1', 10), ('Product3', 12)]

# [List Comprehensions]
# Note (Formula): [expression for item in items]
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
prices = [item[1] for item in items]  # Get the price of each item (map)
print(prices)  # [10, 9, 12]

# Filter items with price >= 10
filtered = [item for item in items if item[1] >= 10]
print(filtered)  # [('Product1', 10), ('Product3', 12)]

# [Zip Function]
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Combine 2 lists
print(list(zip(list1, list2)))  # [(1, 10), (2, 20), (3, 30)]

# [Stacks] (LIFO)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])  # 2 - To get the first item at the top
if not browsing_session:
    print("disable")

# [Queues] (FIFO)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("empty")

# [Tuples] - Read-only list / immutable
point = (1, 2)
print(type(point))  # <class 'tuple'>

point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("10 exists")
else:
    print("10 does not exist")

# [Swapping Variables]

# [Arrays]

# [Sets]

# [Dictionaries]

# [Dictionary Comprehensions]

# [Generator Expressions]

# [Unpacking Operator]

# [Exercise]
