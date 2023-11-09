#single level inheritance:
class Address:
    __address : str = " "
    def addAddress(self,address):
        self.__address =address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName : str = " "
    __lastName : str = " "
    __surName : str = " "
    def setName(self,fName : str, lName : str, sName : str = " "):
        self.__firstName = fName
        self.__surName = sName
        self.__lastName = lName
    def __nameFormat(self):
        return f'{self.__firstName} {self.__lastName} {self.__surName}'
    def getFullName(self):
        return self.__nameFormat()
emp = Employee()
emp.setName(fName = "sai", sName = "G", lName = " sunder")
emp.addAddress("Hyderabad")
print(emp.getFullName())
print(emp.getAddress())

#multi level inheritance:
class Address:
    __address : str = " "
    def addAddress(self,address):
        self.__address =address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName : str = " "
    __lastName : str = " "
    __surName : str = " "
    def setName(self,fName : str, lName : str, sName : str = " "):
        self.__firstName = fName
        self.__surName = sName
        self.__lastName = lName
    def __nameFormat(self):
        return f'{self.__firstName} {self.__lastName} {self.__surName}'
    def getFullName(self):
        return self.__nameFormat()
class perminentEmployee(Employee):
    __sai : int = 30000
    def salca(self)-> float:
        return 12*self.__sal
Emp = perminentEmployee()
emp.setName(fName = "Aamani", sName = "M", lName= "Maruboina")
emp.addAddress("Hyderabad")
print(emp.getFullName())
print(emp.getAddress())

#hirerical inheitance:
class Address:
    __address : str = " "
    def addAddress(self,address):
        self.__address =address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName : str = " "
    __lastName : str = " "
    __surName : str = " "
    def setName(self,fName : str, lName : str, sName : str = " "):
        self.__firstName = fName
        self.__surName = sName
        self.__lastName = lName
    def __nameFormat(self):
        return f'{self.__firstName} {self.__lastName} {self.__surName}'
    def getFullName(self):
        return self.__nameFormat()
class perminentEmployee(Employee):
    __sal : int = 30000
    def salcal(self)-> str:
        return f' salcal per year : (12 * self.__sal)'
class contractEmployee(Employee):
    __hr_pay : int =500
    def salcal(self,hrs : int)->str:
        return f'salcal for (hrs) hrs : self.__hr_pay * hrs)'
pemp =perminentEmployee()
pemp.setName(fName = "Aamani", sName = "M", lName = "MAruboina")
pemp.addAddress("Hyderabad")
print(emp.getFullName())
print(emp.getAddress())
print(pemp.salcal())

cemp =contractEmployee()
cemp.setName(fName = "Aamani", sName = "M", lName = "MAruboina")
cemp.addAddress("Hyderabad")
print(cemp.getFullName())
print(cemp.getAddress())
print(cemp.salcal(20))