import random as r
from string import ascii_uppercase
word = "test".upper()
dotted_word = ["_" for i in word]
max_tries = 3
already_checked = list()
tries = 0
lost = False

def find_indexes(char, word):
    if char in word:
        return [i for i in range(0, len(word)) if word[i] == char]
    else:
        return None

def update_dottedword(word, char, dotted_word):
    for i in find_indexes(char, word):
        dotted_word[i] = char
        already_checked.append(char)
    return dotted_word

def output(dotted_word):
    return " ".join(dotted_word)

def check_win(dotted_word, word):
    if dotted_word == list(word):
        return True
    else:
        return False
        
#game loop
while True:
    guess = input("entre une lettre: ").upper()
    if len(guess) > 1 or guess not in ascii_uppercase or guess  in already_checked:
        print("tu dois entrer une seule lettre et qui n'a jamais été utilisée")
        continue
    if guess in word:
        print("bien jouer, tu as trouvé une lettre correcte")
        print(output(update_dottedword(word, guess, dotted_word)))
        if check_win(dotted_word, word):
            print("you won c'est carré")
            break
    else:
        tries += 1
        print(f'mince tu as fais faux il te reste : {max_tries - tries} essais')
        print(output(dotted_word))
        if max_tries == tries:
            print("tu as perdu le sang")
            break
