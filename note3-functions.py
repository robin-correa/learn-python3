# Defining Functions
def greet1():
    print("Hi there")
    print("Welcome aboard")


greet1()

# Arguments


def greet2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet2("Robin", "Correa")
greet2("Regina", "Ligutan")

# Types of Functions: Type1 - Carries out task, Type2 - Calculates and return a value, All functions return "None" as default


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Robin")
print(message)

# Keyword Arguments


def increment1(number, by):
    return number + by


print(increment1(number=2, by=1))

# Default Arguments


def increment2(number, by=1):
    return number + by


print(increment2(number=2))

# xargs


def multiply(*numbers):  # tuple
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# xxargs - to transform values into dictionary


def save_user(**user):
    print(user)  # Dictionary / Object
    # print(user["id"])  # ID
    # print(user["name"])  # Name


save_user(id=1, name="Robin", age=28)  # {'id': 1, 'name': 'Robin', 'age': 28}

# Exercise


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


print(fizz_buzz(21))  # Fizz
