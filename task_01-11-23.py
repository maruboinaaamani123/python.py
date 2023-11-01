#Global scope(public scope):
class Employee:
    firstName : str ="Aamani"
    lastName : str ="Maruboina"
emp =Employee()
print(emp.firstName)
print(emp.lastName)

#partial private(protected):
class Employee:
    _firstName : str ="Aamani"
    _lastName : str ="Maruboina"
emp=Employee()
print(emp._firstName)

#srictly private
'''
class Employee:
    __firstName : str ="Aamani"
    __lastName : str ="Maruboina"
emp=Employee()
print(emp.__lastName)'''

#Global Variable
def fullName():
    global fName
    lname ="Maruboina"
    fName ="Aamani"
fullName()
print(fName)
#print(lName)


#Abstraction
class Employee:
    __fname : str ="Aamani"
    __lname : str ="Maruboina"
    def fullname(self):
        return self.__fname+" "+self.__lname
emp=Employee()
emp.__fname = "ABC"
print(emp.fullname())


