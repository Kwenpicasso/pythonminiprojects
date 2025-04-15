import random
print("WORD SCRAMBLER")

while True:
    value = input("Enter a word to be scrambled (or quit): ")
    if value.lower() == 'quit':
        print("Goodbye")
        break
    else :
        letter = list(value)
        random.shuffle(letter)
        print(f"scrambled: {''.join(letter)}")
        
