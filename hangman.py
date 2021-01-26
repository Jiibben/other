import random as r
from string import ascii_uppercase
word = "test".upper() # selectionne le mot que le jouer doit trouver (et le change en majuscule)
dotted_word = ["_" for i in word] # crée un mot en underscore (_ _ _ _ ) en se basant sur la variable word
max_tries = 3 #essais maximum avant d'être "pendu"
already_checked = list() #crée une liste des lettres deja utilisée
tries = 0 #essais déjà fais

# retourne une liste des indexes ou la lettre (char) à été trouvée dans (word)
def find_indexes(char, word):
    if char in word:
        return [i for i in range(0, len(word)) if word[i] == char]
    else:
        return None

# change les underscores du mot en lettre selon le charactère donné
def update_dottedword(word, char, dotted_word):
    for i in find_indexes(char, word):
        dotted_word[i] = char
        already_checked.append(char)
    return dotted_word

# affiche le mot de manière jolie (change la liste en string)
def output(dotted_word):
    return " ".join(dotted_word)

# utile pour voir si le joueur à gagner
def check_win(dotted_word, word):
    if dotted_word == list(word):
        return True
    else:
        return False
        
#game loop
while True:
    guess = input("entre une lettre: ").upper()
    if len(guess) > 1 or guess not in ascii_uppercase or guess in already_checked:
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
