print("😎TEXT CAPITALIZER😎")
value = input("Enter a text🥴: ")
print("1.UPPERCASE😎")
print("2.lowercase😎")
print("3.Title Case😎")
print("4.Sentence case😎")
new_value = input("Choose a format from (1-4): ")

if new_value == "1":
    upper = value.upper()
    print(f"{upper}")
elif new_value == "2":
    lower = value.lower()
    print(f"{lower}")
elif new_value == "3":
    title = value.title()
    print(f"{title}")
elif new_value == "4":
    cap = value.capitalize()
    print(f"{cap}")
