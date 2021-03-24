#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import colorama
from colorama import Fore
from colorama import Style

choix = ["casserole", "cuillere", "patate", "souris", "anticonstitutionnellement", "voiture", "nintendo", "apple", "stylo", "zebre", "feuille", "table", "xylophone", "cuisine", "python", "vin", "echelle", "github", "baccalaureat", "pendu"]

solution = random.choice(choix)

tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print("")
print(Fore.BLUE + Style.BRIGHT + ">> Bienvenue " + Fore.GREEN + "dans " + Fore.YELLOW + "le " + Fore.RED + "pendu <<" + Style.RESET_ALL)
print("")
print("------------------------------------------------------------------")

while tentatives > 0:
  print("\n-> Mot à deviner : ", affichage)
  proposition = input(Fore.GREEN + "Proposez une lettre : " + Style.RESET_ALL)[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("")
      print(Fore.YELLOW + "-> Bien vu !" + Style.RESET_ALL)
      print("")

  else:
    tentatives = tentatives - 1
    print("")
    print(Fore.RED + "-> Faux\n" + Style.RESET_ALL)
    if tentatives==0:
        print(Fore.RED + " ==========Y= " + Style.RESET_ALL)
    if tentatives<=1:
        print(Fore.RED + " ||/       |  " + Style.RESET_ALL)
    if tentatives<=2:
        print(Fore.RED + " ||        0  " + Style.RESET_ALL)
    if tentatives<=3:
        print(Fore.RED + " ||       /|\ " + Style.RESET_ALL)
    if tentatives<=4:
        print(Fore.RED + " ||       / \ " + Style.RESET_ALL)
    if tentatives<=5:
        print(Fore.RED + "/||           " + Style.RESET_ALL)
    if tentatives<=6:
        print(Fore.RED + "==============\n" + Style.RESET_ALL)

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print("")
      print("")
      print(Fore.YELLOW + ">>> Gagné! <<<" + Style.RESET_ALL)
      break

print("")
print(Fore.BLUE + Style.BRIGHT + " Le mot était", "\"", solution, "\"" + Style.RESET_ALL)
print("")
print(Fore.RED + "\n    * Fin de la partie *    " + Style.RESET_ALL)
print("")

print("")
input("ENTRÉE pour quitter le programme")
