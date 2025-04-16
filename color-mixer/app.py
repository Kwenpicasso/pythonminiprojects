import random
print("COLOR MIXER")

mixed = ['pink', 'orange', 'wine',
         'red', 'blue', 'green']

while True:
    first_color = input("Enter your first color: ")
    second_color = input("Enter your second color: ")
    mixed_color = random.choice(mixed)

    print(
        f"When you mix {first_color} and {second_color} you get {mixed_color} !")

    value = input("Mix more colors? (y/n):")
    if value.lower() != 'y':
        print("Goodbye")
        break
