# age = 2
# message = 'eligible' if age >= 20 else 'not eligbile'
# print(message)


# high_income = False
# budget = True
# student = True

# if (high_income or budget) and not student:
#     print('student')
# else:
#     print("not a student")

# # and operator
# status = 'rich' if high_income and budget else 'broke'
# # or operator
# status = 'rich' if high_income or budget else 'broke'
# print(status)


# age should be between 18 to 30
# age = 2
# if age >= 18 and age < 30:
#     print('passed')
# else:
#     print("failed")

def kwen(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(kwen(9, 2, 5, 8))
