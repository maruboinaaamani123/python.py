#method over loading
class caluclation:
    def add(self, a:int, b:int):
        print(a+b)
    def add(self, a:int, b:int, c:int=0):
        print(a+b+c)
cal = caluclation()
cal.add(1,2,3)

#method overriding:
class Employee:
    __amt=40000
    def sal(self):
        return self.__amt*4

class ContractEmployee(Employee):
    __hrpay=1000
    __hrs=10

    def sal(self):
        return self.__hrpay*self.__hrs

emp=ContractEmployee()
print(emp.sal())

#constuctor
#1.default constuctor
class Employee:
    def fullName(self,fName,lName):
        print(fName+lName)
emp=Employee()
emp.fullName("Aamani"," Maruboina")

#parameterless constuctor;
class Employee:
    def __init__(self):
        pass
    def fullName(self,fName,lName):
        print(fName,lName)
emp=Employee()
emp.fullName("Aamani","Maruboina")

#paramerterized constuctor;
class Employee:
    __fName : str =" "
    __lName : str =" "
    def __init__(self,fName,lName):
        self.__fname =fName
        self.__lname =lName
    def fullName(self):
        print(self.__fname + self.__lname)
emp=Employee("sujatha", " Maruboina")
emp.fullName()

