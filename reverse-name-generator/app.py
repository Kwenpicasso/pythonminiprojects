print("reverse name generator")
while True:
    value = input("Enter a name: ")
    if not value:
        break
    reversed_name = value[::-1]
    print(f"Your reversed name is : {reversed_name}")
    print(f"in a parallel universe , they call you {reversed_name.title()}!")


    retry_value = input("Try another name?(y/n): ")
    if retry_value.lower() != 'y':
       break