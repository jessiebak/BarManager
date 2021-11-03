class Employee:
    __employeeID= int
    __employeeName= ""
    __employeeStatus= ""
    __employeeSchedule= ""
    
    def __init__(self, eID, eName, eStatus, eSchedule):
        self.__employeeID = eID
        self.__employeeName = eName
        self.__employeeStatus = eStatus
        self.__employeeSchedule = eSchedule
    
    def getEmployeeID(self):
        return self.__employeeID
    def getEmployeeName(self):
        return self.__employeeName
    def getEmployeeStatus(self):
        return self.__employeeStatus
    def getEmployeeSchedule(self):
        return self.__employeeSchedule
    
    def setEmployeeName(self, value):
        self.__employeeName= value
    def setEmployeeStatus(self, value):
        self.__employeeStatus= value
    def setEmployeeSchedule(self, value):
        self.__employeeSchedule= value
        
