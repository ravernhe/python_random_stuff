#!/usr/bin/python
# -*-coding:utf-8 -*

from data import *
from operator import itemgetter
import requests
from bs4 import BeautifulSoup

def get_all_lettre(nb_lettre):
    lettres = input("Ajoute une lettre (\"*\" pour joker): ")
    lettres = lettres.lower()
    for lettre in lettres:
        if not lettre == "*" and (len(lettre) != 1 or not (lettre >= 'a' and lettre <= 'z'))\
            or len(lettres) != nb_lettre:
            print("Lettres invalide.")
            return get_all_lettre(nb_lettre)
    return (lettres)

def get_nb_lettre():
    nb = input("Quel est ton nombre de lettre? ")
    nb = nb.lower()
    if len(nb) != 1 or not (nb >= '0' and nb <= '9'):
        print("Nombre invalide.")
        return get_nb_lettre()
    else:
        return (nb)

def get_lettre():
    nb_lettre = get_nb_lettre()
    nb_lettre = int(nb_lettre)
    l_lettre = get_all_lettre(nb_lettre)
    for l in l_lettre:
        list_lettre.append(l)
    return nb_lettre

def get_request(index):
    nb = input("Nombre de lettre réponse ou 'n' pour quitter : ")
    nb = nb.lower()
    if len(nb) != 1 or not ((nb > '1' and nb <= str(index + 1) or nb == 'n')):
        print("Nombre invalide.")
        return get_request(index)
    else:
        return (nb)

def count_word(index, nb_lettre):
    i = 0
    all_word = []
    for each in true_word:
        count = 0
        tmp = each
        if len(each) == index:
            for lettre in list_lettre:
                if lettre == "*":
                    count += 1
                if lettre in tmp:
                    count += 1
                    tmp = tmp.replace(lettre, '', 1)
            if index == nb_lettre + 1 and count + 1 == index:
                i += 1
                all_word.append(each)
            elif count == index:
                i += 1
                all_word.append(each)
    return Word(index, i, all_word)


def find_word(list_lettre, nb_lettre):
    index = nb_lettre + 1
    while index > 1:
        listing.append(count_word(index, nb_lettre))
        index -= 1

def get_definition():
    print("\nLa définiton ne marche pas pour les verbes conjugés.\n")
    find_def = input("De quel mot veux-tu la définiton? ('n' pour aucun) : ").lower()
    if find_def != 'n' :
        reponse = requests.get(url + find_def)
        if reponse.ok :
            soup = BeautifulSoup(reponse.text, 'lxml')
            defintion = soup.find_all('ul')[0].text
            print(defintion)
        else :
            print("Erreur pour trouver la définition.")

def get_result(nb_lettre):
    key_press = 'o'
    sort_point = {}
    request = get_request(nb_lettre)
    if request != 'n':
        request = (nb_lettre + 1) - int(request)
    while request != 'n':
        for each in listing[request].list_word:
            puntos = 0
            for l in each:
                puntos += value_lettre[l]
            sort_point[puntos] = each
        x = 0
        if listing[request].nb_word > 0:
            for i in sorted (sort_point): 
                print("Mot : \"{}\" pour {} puntos.".format(sort_point[i], i))
                x += 1
        print("Pour {} lettres, il y'a {} mots.".format(listing[request].index, x))
        if x != 0:
            get_definition()
        request = get_request(nb_lettre)
        if request != 'n':
            request = (nb_lettre + 1) - int(request)
        sort_point.clear()
