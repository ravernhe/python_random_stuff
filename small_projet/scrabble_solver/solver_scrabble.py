#!/usr/bin/python
# -*-coding:utf-8 -*

from data import *
from func import *

continue_game = 'o'

while continue_game != 'n':
    nb_lettre = get_lettre()
    if nb_lettre == 1:
        print("Ta lettre est : {}".format(list_lettre))
    else:
        print("T'es lettres sont : {}".format(list_lettre))
    find_word(list_lettre, nb_lettre)
    get_result(nb_lettre)

    """On clearn la liste avec de relancer une partie"""  
    list_lettre.clear()
    listing.clear()
    continue_game = input("Veux-tu continuer (O/N) ? ")
    continue_game = continue_game.lower()

    