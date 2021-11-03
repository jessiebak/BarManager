class Products: 

	__name = ""
	__price = 0 

	def __init__(self, name, price) -> None:
		self.__name = name  
		self.__price = price 
	
	def __str__(self) -> str:
		return self.DisplayProductsInfos()

	def getName(self):
		return self.__name
	def getPrice(self): 
		return self.__price

	def setName(self, value): 
		self.__name = value

	def setPrice(self, value): 
		self.__price = value

	def DisplayProductsInfos(self):
		print(f"------------ Fiche produit pour {self.getName()} ------------------------")
		for item in self.__dict__: 
			print(f"{item} : {self.__dict__[item]}")
		print ("-------------------------------")

class Drinks(Products): 
	__quantity = 0 # en cl
	__brand = ""  #Marque
	__isBottle = False 
	__isCan = False 	

	def __init__(self, name, price, quantity, brand, isB0ottle=False, isCan= False) -> None:
		super().__init__(name, price)

		self.__quantity = quantity 
		self.__brand = brand
		self.__isBottle = isB0ottle
		self.__isCan = isCan 
	


class Beers(Drinks): 
	
	__productionCountry = "" #pays de production 
	__alcoholLevel = 0.0 #Niveau d'alcool en % 
	__ingredients = [] #liste des ingrédients 
	__isTap = False 

	def getProductionCountry(self):
		return self.__productionCountry
	
	def getAlcoholLevel(self):
		return self.__alcoholLevel 
	
	def getIngredients(self): 
		return self.__ingredients 
	
	def getIsTap(self): 
		return self.__isTap
	

	def __init__(self, name, price, quantity, alcoholLevel) -> None:
		super().__init__(name, price, quantity, alcoholLevel)
		self.__quantity = quantity 
		self.__alcoholLevel = alcoholLevel 

class SoftDrinks(Drinks): 
	pass


chouffe = Beers("Chouffe", 4.5,75,8) 
coca = SoftDrinks("Coca-Cola", 2, 100, "Coca-Cola",True, True)


if __name__ == '__main__': 
	coca.DisplayProductsInfos()

	chouffe.DisplayProductsInfos()

