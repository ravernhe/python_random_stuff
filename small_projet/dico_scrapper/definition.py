#!/usr/bin/python
# -*-coding:utf-8 -*

import requests
from bs4 import BeautifulSoup

mot = input("De quel mot veux-tu la définition? ").lower()
url = 'https://www.le-dictionnaire.com/definition/' + mot

reponse = requests.get(url)

if reponse.ok :
    soup = BeautifulSoup(reponse.text, 'lxml')
    defintion = soup.find_all('ul')[0].text
    print(defintion)
else :
    print("Erreur")