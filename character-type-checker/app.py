print("Character type checker")
value = input("Enter a single character: ")
if value.isalpha():
    print("This is a letter")
elif value.isdigit():
    print("This is a number")
else:
    print("This is a special charater")
