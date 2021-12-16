from products import Products, Beers, SoftDrinks
import xlsxwriter as xls 

class Menu():
	__product = ''
	__list_of_products = [] 

	def __init__(self) -> None:
		pass 
	
	

	def getProduct(self):
		return self.__product
	def getListOfProducts(self): 
		return self.__list_of_products

	
	
	def DisplayMenu(self):
		if len(self.__list_of_products) == 0:
			print("Aucun élément dans le menu, veuillez d'abord insérer des produits")
		else : 
			print('Au Menu du Bar : ')
			for item in self.__list_of_products:
				print(item.DisplayProductsInfos())
	def __str__(self) -> str:
		return self.DisplayMenu()

	def AddToMenu(self,*item):
		global sheet1
		row = 2
		column = 0
		for element in item:
			self.__list_of_products.append(element)	 
			for i in [item[0].getName(), item[0].getPrice(), item[0].getAlcoholLevel()]:
				sheet1.write(row,column,"Coucou") 
				column+=1 
			column = 0
			row+=1 


			
		
		
		



	def DeleteOfMenu(self):
		if len(self.__list_of_products) == 0: 
			print("Aucun élément dans le menu, veuillez d'abord insérer des produits")
		else: 	
			print("Sélectionnez le numméro du produit à retirer du menu")
			for number, item in enumerate(self.__list_of_products,1): 
				print(number, item.getName())
			index = int(input("Votre choix : ")) + 1
			deleteditem = self.__list_of_products.pop(index)
			print(f"Le produit suivant vient d'être supprimé: {deleteditem}")


def createMenu(_menu): 
	global sheet1 
	
	Titles = ["Produits", "Prix", "% Alc"]
	row =0
	column = 0 

	for title in Titles:
		sheet1.write(row, column, title)
		column+=1 
		
		# for i, product  in enumerate(Mymenu.getListOfProducts()):

	return _menu

excelMenu = xls.Workbook("Menu.xlsx")
sheet1 = excelMenu.add_worksheet("Menu du Bar")
excelMenu = createMenu(excelMenu)



if __name__ == '__main__': 
	pass