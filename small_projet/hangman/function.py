#!/usr/bin/python
# -*-coding:utf-8 -*

import os
import pickle
from random import choice
from data import *

def get_score():
    if os.path.exists(name_score_file):
        score_file = open(name_score_file, "rb")
        my_depickler = pickle.Unpickler(score_file)
        scores = my_depickler.load()
        score_file.close()
    else:
        scores = {}
    return scores

def save_score(scores):
    score_file = open(name_score_file, "wb")
    my_pickler = pickle.Pickler(score_file)
    my_pickler.dump(scores)
    score_file.close()

def get_user():
    user_name = input("Username : ")
    user_name = user_name.capitalize()
    if not user_name.isalnum() or (len(user_name) < 1 and len(user_name) > 12):
        print("Username non comforme.")
        return get_user()
    else:
        return user_name

def get_letter():
    lettre = input("Choissit une lettre : ")
    lettre = lettre.lower()
    if len(lettre) > 1 and not lettre.isalpha:
        print("Lettre invalide.")
        return get_letter()
    else:
        return (lettre)

def choose_word():
    return choice(word)

def get_hidden_word(full_word, founded_letter):
    hidden_word = ""
    for lettre in full_word:
        if lettre in founded_letter:
            hidden_word += lettre
        else:
            hidden_word += "_"
    return hidden_word

