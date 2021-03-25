#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import colorama
from colorama import Fore
from colorama import Style

wordlist = []
with open("english.txt") as file:
    for line in file:
     wordlist.append(line)
wordlist = list(map(lambda x : x[:-1], wordlist))

solution = random.choice(wordlist)

tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print("")
print(Fore.BLUE + ">> Welcome " + Fore.GREEN + "to " + Fore.YELLOW + "the " + Fore.RED + "hangman's game <<" + Style.RESET_ALL)
print("")
print("------------------------------------------------------------------")

while tentatives > 0:
  print("\n-> Word to guess : ", affichage)
  proposition = input(Fore.GREEN + "Submit a letter : " + Style.RESET_ALL)[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("")
      print(Fore.YELLOW + "-> Well done !" + Style.RESET_ALL)
      print("")

  else:
    tentatives = tentatives - 1
    print("")
    print(Fore.RED + "-> Wrong\n" + Style.RESET_ALL)
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
      print(Fore.YELLOW + ">>> You won! <<<" + Style.RESET_ALL)
      break

print("")
print(Fore.BLUE + Style.BRIGHT + " The word was", "\"",solution,"\"" + Style.RESET_ALL)
print("")
print(Fore.YELLOW + "\n    * End of the game *    " + Style.RESET_ALL)
print("")

print("")
input("-> ENTER to quit")
