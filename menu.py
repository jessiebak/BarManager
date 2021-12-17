from products import Products, Beers, SoftDrinks


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
		
		for element in item:
			self.__list_of_products.append(element)	 
			

			
		
		
		



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


if __name__ == '__main__': 
	pass