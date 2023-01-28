# [Handling Exceptions]

# try:
#     age = int(input("Age: "))
# except ValueError as e:
#     print("You didn't enter a valid age")
#     print(e)
#     print(type(e))
# else:
#     print("No exceptipons were thrown.")
# print("Execution continues.")

# [Handling Different Exceptions]

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as e:
#     print("You didn't enter a valid age")
# else:
#     print("No exceptipons were thrown.")

# [Cleaning Up]

# try:
#     file = open("test_file.py", "w", encoding="utf8")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as e:
#     print("You didn't enter a valid age")
# else:
#     print("No exceptipons were thrown.")
# finally:
#     file.close()

# [The With Statement]
# try:
#     with open("test_file.py", "w", encoding="utf8") as file:
#         print("File opened.")
#         age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as e:
#     print("You didn't enter a valid age")
# else:
#     print("No exceptipons were thrown.")
# finally:
#     file.close()
#     print("File closed")

# [Raising Exceptions]


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
