class Employee:
    __employeeID= 0
    __employeeName= ""
    __employeeStatus= ""
    __employeePost= ""
    __employeeSchedule= []
    __employeeSalary= 0
    
    def __init__(self, eID, eName, eStatus,ePost, eSchedule, eSalary):
        self.__employeeID = eID
        self.__employeeName = eName
        self.__employeeStatus = eStatus
        self.__employeePost = ePost
        self.__employeeSchedule = eSchedule
        self.__employeeSalary = eSalary
    
    def getEmployeeID(self):
        return self.__employeeID
    def getEmployeeName(self):
        return self.__employeeName
    def getEmployeeStatus(self):
        return self.__employeeStatus
    def getEmployeePost(self):
        return self.__employeePost
    def getEmployeeSchedule(self):
        return self.__employeeSchedule
    def getEmployeeSalary(self):
        return self.__employeeSalary
    
    def setEmployeeName(self, value):
        self.__employeeName = value
    def setEmployeeStatus(self, value):
        self.__employeeStatus = value
    def setEmployeePost(self, value):
        self.__employeePost = value
    def setEmployeeSchedule(self, value):
        self.__employeeSchedule = value
    def setEmployeeSalary(self, value):
        self.__employeeSalary = value
        


class Client :
	__name = "undefined"
	__id = "undefined"
	__listing = "undefined"
	__langue = "undefined"
	
	def __init__(self, n, i, l, lg):
		self.__name = n 
		self.__id = i
		self.__listing = l
		self.__langue= lg
		

	def GetName(self):
		return self.__name 
	def GetId(self):
		return self.__id 
	def GetListing(self):
		return self.__listing 
	def GetLangue(self):
		return self.__langue
	
	

	def SetName(self, value):
		self.__name = value 
	def SetId(self, value):
		self.__id = value 
	def SetListing(self, value):
		self.__listing = value 
	def SetLangue(self, value):
		self.__langue = value 
	
	
# Métode :
	def AveragePrice(self):
		average =0
		for i in range(len(self.__listing)):
			average += self.__listing[i][0].getPrice() * self.__listing[i][1]
		average=average/len(self.__listing)
		return average

	def TotalPriceOfTheOrder(self):
		langue = self.__langue
		totalWithReduction = 0
		if langue == "FR":
			for i in range(len(self.__listing)):
				totalWithReduction+= self.__listing[i][0].getPrice() * self.__listing[i][1]
		elif langue == "EN": 
			for i in range(len(self.__listing)):
				totalWithReduction+= self.__listing[i][0].getPrice() * self.__listing[i][1] * 1.17			
		return round(totalWithReduction, 2)

	def paiement(self,montant):
		langue = self.__langue
		while True :
			if langue == "FR":
				try :
					client_money = float(input(f"Vous nous devez  donc {montant} euros \n Veuillez introduire votre argent"))
				except:
					print("Il faut un chiffre")
				if client_money > montant: 
					print(f"voici {client_money - montant} € de retour")
					break
				elif client_money== montant:
					print(f"Merci pour le compte juste")
					break
				else: 
					print(f"Désolé mais ce n'est pas assez ! Il vous manque {montant - client_money} euros. Reesayer")
			if langue == "EN":
				client_money = float(input(f"Vou have to pay {montant} dollars \n Enter your money"))
				if client_money > montant: 
					print(f"Here are {client_money - montant} dollars in change")
					break
				elif client_money== montant:
					print(f"Thanks for the exact amount")
					break
				else: 
					print(f"It's not enough ! You still owe us  {montant - client_money} dollars. Try again")

	def PrintReceipt(self):
			langue = self.__langue
			if langue == "FR":
				print("Tiquet de caisse.")
				print("vos produits :")
				
				for j in range(len(self.__listing)):
						
					print(self.__listing[j][0].getName() , " " , self.__listing[j][0].getPrice(), "€", "(x", self.__listing[j][1], ")")		
					 		
				print("prix total :", self.TotalPriceOfTheOrder(), "€")
				self.paiement(self.TotalPriceOfTheOrder())
			elif langue == "EN":
				print("Receipt.")
				print("Your products:")
				
				for j in range(len(self.__listing)):
						
					print(self.__listing[j][0].getName() , " " , round(self.__listing[j][0].getPrice()*1.17, 2), "$", "(x", self.__listing[j][1], ")")		
									
				print("Total price :", self.TotalPriceOfTheOrder(), "$")
				self.paiement(self.TotalPriceOfTheOrder())				
				








			

	def addProduct(self, *__item):
		for i in __item: 
			_listing = self.__listing.append(i)			 			
		return _listing 