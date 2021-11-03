import openfoodfacts
from products import * 
from menu import Menu 
def ChooseMenu():
	print("Bienvenue dans ce programme de gestion de bar. \n Que souhaitez-vous faire? ")

	_choice = int(input(" 1. Créer un menu pour votre bar ?  \n 2. Afficher le menu.  \n 3. Faire payer votre client. "))

	return _choice 

 
# choice = ChooseMenu() 

Mymenu = Menu()

Mymenu.AddToMenu(chouffe,coca)
Mymenu.DeleteOfMenu()


