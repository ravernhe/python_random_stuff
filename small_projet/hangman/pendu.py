#!/usr/bin/python
# -*-coding:utf-8 -*

from data import *
from function import *

scores = get_score()
user = get_user()

if user not in scores.keys():
    scores[user] = 0


continue_game = 'o'

while continue_game != 'n':
    print("Joueur {0} : {1} puntos.".format(user, scores[user]))
    to_find = choose_word()
    founded_letter = []
    search_word = get_hidden_word(to_find, founded_letter)
    nb_try = nb_coup

    while search_word != to_find and nb_try > 0:
        print(search_word)
        print("Try : " + str(nb_try))
        lettre = get_letter()
        if lettre in founded_letter:
            print("Tu as déjà trouver : " + lettre)
        elif lettre in to_find:
            founded_letter.append(lettre)
            print("Bien jouer.")
        else :
            nb_try -= 1
            print("La lettre ne se trouve pas dans le mot")
        search_word = get_hidden_word(to_find,founded_letter)

    if search_word == to_find:
        print("Tu as trouvé le mot : " + to_find)
    else:
        print("Looser..")
    
    scores[user] += nb_try

    continue_game = input("Veux-tu continuer (O/N) ? ")
    continue_game = continue_game.lower()

save_score(scores)
print("Tu finis cette partie avec un score de : {0}".format(scores[user]))