# Comparison operator
print(21 == "21")  # False

# Conditional Statements
temperature = 21
if temperature > 30:
    print("It's warm")  # under if condition
    print("Drink water")  # under if condition
elif temperature > 20:
    print("It's nice")  # under elif condition
else:
    print("It's cold")  # under elif condition
print("Done")  # outside if

# Ternary Operator
age = 21

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical Operators: and, or, not
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# Chaining Comparison
age = 17
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# For loops
for number in range(3):  # starts with 0 to 2
    print("Attempt", number)

for number in range(1, 3):  # starts with 1 to 2
    print("Attempt", number)

# For .. Else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    # will only execute if successful = False / if not break
    print("Attempted 3 times and failed")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables
for x in "Python":  # iterable string: P y t h o n
    print(x)

for x in [1, 2, 3, 4]:  # iterable list: 1, 2, 3, 4
    print(x)

# While Loops
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# Infinite Loops
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# Exercise (even numbers)
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even number")
