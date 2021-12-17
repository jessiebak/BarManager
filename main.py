
from products import * 
from menu import *
from menu import excelMenu
import xlsxwriter as xls 
from staff import Client
import os
import time


clientID = 0

def CreateClient():
	global clientID
	languageClient = int(input("1 : Bonjour parlez vous français ? \n  2 : Do you speak english? \n"))
	if languageClient == 1:
		_langue = "FR"
		print("Bienvenue dans notre bar le Good News\n")
		nameClient = input("Puis-je avoir votre nom?: \t")
	elif languageClient == 2:
		_langue = "EN"
		print("Welcome in to the Bar the Good News bar")
		nameClient = input("Could I have your name please ? \t")
	clientID += 1
	client = Client(nameClient, clientID, [], _langue)
	return client

def ChooseProduct(client, AllProduct):
	_listChoose = []
	if client.GetLangue() == "FR":
		print("Veuillez choisir vos produits dans la liste suivante : \n")
		for number, item in enumerate(AllProduct):
			print("n°", number + 1, ":", item.getName())
		_choose = int(input("Votre choix : \t")) - 1
		_quantity = int(input("Combien en voulez-vous :\n"))
		_listChoose.append(AllProduct[_choose])
		client.addProduct([_listChoose[0], _quantity])
		client.PrintReceipt()
	elif client.GetLangue() == "EN":
		print("Choose your product in the next list: \n")
		for number, item in enumerate(AllProduct):
			print("n°", number + 1, ":", item.getName())
		_choose = int(input("Your choose: \t ")) - 1
		_quantity = int(input("How many do you want:\n"))
		_listChoose.append(AllProduct[_choose])
		client.addProduct([_listChoose[0], _quantity])
		client.PrintReceipt()



# import interface
def ChooseMenu():
	_choice = int(input(" 1. Créer un menu pour votre bar ?  \n 2. Afficher le menu.  \n 3. Faire payer votre client. \n 0. Quitter\n\n Entrez votre choix : \t "))
	return _choice 
	


choice = -1000
print("Bienvenue dans ce programme de gestion de bar. \n Que souhaitez-vous faire? ")

while choice != "0":
	choice = ChooseMenu()	
	print("---------------- Bar Manager-----------------")
	if choice == 1: 
		createMenu(excelMenu)
		myMenu= Menu() 
		# myMenu.AddToMenu(chouffe,coca)
		if len(myMenu.getListOfProducts()) == 0: 
			print("Le Menu est vide pour l'instant")
			see_content = int(input("Voulez-vous voir la listes des produits disponibles chez votre fournisseur  aifin de les ajouter? \n 1. oui \n 2. Non  \n\n Votre réponse : \t"))
			if see_content == 1:
				print ("Voici la liste de  tous les produits disponibles chez votre fournisseur")
				
				for i in Products.add(): 
					print(i)
				# for item in Products.__dict__:
				# 	print(item)
				break
		else: 
			print("Voici les produits déjà disponible dans votre magasin")
			myMenu.DisplayMenu()
				
			
		# os.startfile(f"{os.path.dirname((__file__))}\Menu.xlsx")

	elif choice  == 2: 

		Mymenu = Menu()
		Mymenu.DisplayMenu()
	elif choice == 3:
		clientOne = CreateClient()
		ChooseProduct(clientOne, AllProducts)
	elif choice == 4: 
		print("Au revoir et à bientôt dans Bar Manager")

excelMenu.close
