# Formatted string
import math
first_name = "Robin"
last_name = "Correa"
full_name = f"{first_name} {last_name}"
print(full_name)

# String methods
course = "Python Programming"
print(course.upper())  # PYTHON PROGRAMMING

print(course.lower())  # python programming
print(course.title())  # Python Programming
print(course.rstrip())   # Python Programming (remove spaces at the right)
print(course.find("programming1"))  # index: 7 / -1 if not found
print(course.replace("P", "R"))  # Rython Programming
print("Pro" in course)  # boolean: True
print("PHP" in course)  # boolean: False


# Numbers
print(round(20.9))  # 21
print(abs(-21))  # 21
print(math.ceil(20.1))  # 21

# Type Conversion
x = "20"
# y = x + 1 - Error
y = int(x) + 1  # - Correct
# print(type(x))
print(f"x: {x}, y: {y}")
