
from math import e
from products import * 
from menu import *

from staff import Client
from os import system
import time

cls = system("cls")
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
		_choose = -1000
		while 0 < _choose < len(AllProduct+1): 
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
	_choice = int(input(" 1. Modifier le  menu pour votre bar ?  \n 2. Afficher le menu.  \n 3. Faire payer votre client. \n 0. Quitter\n\n Entrez votre choix : \t "))
	return _choice 
	


choice = -1000
print("Bienvenue dans ce programme de gestion de bar. \n Que souhaitez-vous faire? ")

while choice != "0":
	choice = ChooseMenu()	
	print("---------------- Bar Manager-----------------")
	if choice == 1: 
		# createMenu(excelMenu)
		myMenu= Menu() 

		if len(myMenu.getListOfProducts()) == 0: 
			print("Le Menu est vide pour l'instant")
			print("Voulez vous afficher les détails des produits disponibles ou juste le nom des produits")
		
			
			details= 0
			while details not in [1,2]:
				details = int(input("1. Description Détaillées \n  2. Nom des protuis"))
			if details == 1: 	
			# myMenu.AddToMenu(chouffe,coca)
			
				print("Voici la liste de  tous les produits disponibles chez votre fournisseur")
				for i, item in enumerate(AllProducts): 
					print(f"#{i}")
					print(item.DisplayProductsInfos())

					userchoice = -1000
					MenuProducts = []
					while userchoice != 0:
						userchoice = int(input("Quel numéro souhaitez-vous ajouter. \n Mettez 0 pour terminer"))
						if 0 < userchoice <= len(AllProducts):
							MenuProducts.append(AllProducts[userchoice-1])
						elif userchoice == 0: 
							print("Merci bien noté")
							break
						else: 
							print("Désolé ce numéro ne fait pas partie de notre liste")
							details = int(input("1. Description Détaillées \n  2. Nom des produits"))
							
							continue
			elif details == 2: 
				print("Voici la liste de  tous les produits disponibles chez votre fournisseur")
				for i, item in enumerate(AllProducts):
					print(f"n°{i+1} : {item.getName()}")
		userchoice = -1000
		MenuProducts = []
		while userchoice != 0:
			userchoice = int(input("Quel numéro souhaitez-vous ajouter. \n Mettez 0 pour terminer"))
			if 0 < userchoice <= len(AllProducts):
				MenuProducts.append(AllProducts[userchoice-1])
			elif userchoice == 0: 
				print("Merci bien noté")
				break
			else: 
				print("Désolé ce numéro ne fait pas partie de notre liste")
				details = int(input("1. Description Détaillées \n  2. Nom des produits"))
				
				continue

		else: 
			print("Voici les produits déjà disponible dans votre magasin")
			myMenu.DisplayMenu()
				
			
		# os.startfile(f"{os.path.dirname((__file__))}\Menu.xlsx")

	elif choice  == 2: 
		try:  
			print("Veuillez d'abord composer votre menu avant de l'afficher")
			for item in MenuProducts:
				item.DisplayProductsInfos()
		except (UnboundLocalError, NameError): 
			print("Veuillez d'abord composer votre menu avant de l'afficher")

	elif choice == 3:
		try:
			if len(MenuProducts) >0: 
				clientOne = CreateClient()
				ChooseProduct(clientOne, MenuProducts)
		except (UnboundLocalError, NameError): 
			print("Veuillez d'abord composer votre menu avant d'inviter un client à commander")
	elif choice == 4: 
		print("Au revoir et à bientôt dans Bar Manager")

excelMenu.close
