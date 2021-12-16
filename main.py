import openfoodfacts
from products import * 
from menu import *
from menu import excelMenu
import xlsxwriter as xls 
import os
import time

# import interface
def ChooseMenu():
	print("Bienvenue dans ce programme de gestion de bar. \n Que souhaitez-vous faire? ")
	_choice = int(input(" 1. Créer un menu pour votre bar ?  \n 2. Afficher le menu.  \n 3. Faire payer votre client. \n\n Entrez votre choix : \t "))
	return _choice 
	
choice = ChooseMenu() 

if choice == 1: 
	createMenu(excelMenu)
	time.sleep(1)
	os.startfile(f"{os.path.dirname((__file__))}\Menu.xlsx")
	myMenu= Menu()
	myMenu.AddToMenu(chouffe,coca)

elif choice  == 2: 
	Mymenu = Menu()
	Mymenu.DisplayMenu()
elif choice == 3:
	pass

excelMenu.close
