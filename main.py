import openfoodfacts
from products import * 
from menu import *
from menu import excelMenu
import xlsxwriter as xls 
import os
import time

# import interface
def ChooseMenu():
	_choice = int(input(" 1. Créer un menu pour votre bar ?  \n 2. Afficher le menu.  \n 3. Faire payer votre client. \n\n Entrez votre choix : \t "))
	return _choice 
	
choice = ChooseMenu() 

stop = "XXXX"
print("Bienvenue dans ce programme de gestion de bar. \n Que souhaitez-vous faire? ")

while stop != "stop":
	ChooseMenu()	
	print("---------------- Bar Manager-----------------")
	if choice == 1: 
		createMenu(excelMenu)
		myMenu= Menu() 
		myMenu.AddToMenu(chouffe,coca)
		if len(myMenu.getListOfProducts()) == 0: 
			print("Le Menu est vide pour l'instant")
			see_content = int(input("Voulez-vous voir la listes des produits disponibles chez votre fournisseur  aifin de les ajouter? \n 1. oui \n 2. Non  \n\n Votre réponse : \t"))
			if see_content == 1:
				print ("Voici la liste de  tous les produits disponibles chez votre fournisseur")
				for item in Products.__dict__:
					print(item)
				break
		else: 
			print("Voici les produits déjà disponible dans votre magasin")
			myMenu.DisplayMenu()
				
			
		# os.startfile(f"{os.path.dirname((__file__))}\Menu.xlsx")

	elif choice  == 2: 

		Mymenu = Menu()
		Mymenu.DisplayMenu()
	elif choice == 3:
		pass

excelMenu.close
