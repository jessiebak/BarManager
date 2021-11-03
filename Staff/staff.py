class Employee:
    __employeeID= 0
    __employeeName= ""
    __student= False
    __employeePost= ""
    __employeeSchedule= []
    __employeeSalary= 0
    
    def __init__(self, eID, eName, student ,ePost, eSchedule, eSalary):
        self.__employeeID = eID
        self.__employeeName = eName
        self.__student = student
        self.__employeePost = ePost
        self.__employeeSchedule = eSchedule
        self.__employeeSalary = eSalary
    
    def getEmployeeID(self):
        return self.__employeeID
    def getEmployeeName(self):
        return self.__employeeName
    def getEmployeeStatus(self):
        return self.__student
    def getEmployeePost(self):
        return self.__employeePost
    def getEmployeeSchedule(self):
        return self.__employeeSchedule
    def getEmployeeSalary(self):
        return self.__employeeSalary
    
    def setEmployeeName(self, value):
        self.__employeeName = value
    def setEmployeeStatus(self, value):
        self.__student = value
    def setEmployeePost(self, value):
        self.__employeePost = value
    def setEmployeeSchedule(self, value):
        self.__employeeSchedule = value
    def setEmployeeSalary(self, value):
        self.__employeeSalary = value

class Manager:
    
# DB MySQL?
# def AddEmployee
# def RemoveEmployee
# def DisplayEmployee
# def PromoteEmployee
