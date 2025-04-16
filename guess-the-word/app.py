import random
print("WORD SCRAMBLE GAME")
print("Unscramble the the letter to find the word!")
words = ['code', 'boy', 'girl', 'baby', 'game', 'mum']

while True:
    original_word = random.choice(words)
    letter = list(original_word)
    random.shuffle(letter)
    scrambled_letter = "".join(letter)

    print(f"scrambled word is : {scrambled_letter}")
    value = input("what is the word? :")

    if value.lower() == original_word:
        print("correct you win !!!")
    else:
        print(f"sorry the word is {scrambled_letter}")

    play_again = input("play again? (y/n) :")

    if play_again.lower() != 'y':
        print("thanks for playing!")
        break
