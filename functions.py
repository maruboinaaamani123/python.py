#string techinques
#captilize():
#syntax:variable.captilize()
name ="aamani"
print(name.capitalize())

#title():
#syntax:variable.title()
name ="aamani"
print(name.title())

#upper():
#syntax:variable.upper()
name ='aamani'
print(name.upper())

#lower():
#syntax:variable.lower()
name ="AAMANI"
print(name.lower())

#casefold():
#syntax:variable.casefold()
name ="AAMANI"
print(name.casefold())

#swapcase():
#syntax:variable.swapcase()
name ="krishna"
print(name.swapcase())

#string check functions
#isnumeric()
#syntax:variable.isnumeric()
num ="123"
print(num.isnumeric())

#isalpha()
#syntax:variable.isalpha()
name ="Aamnai12"
print(name.isalpha())

#isdigit()
#syntax:variable.isdigit()
num ="123"
print(num.isdigit())

#islower()
#syntax:variable.islower()
name ="AAMANI"
print(name.islower())

#isupper()
#syntax:variable.isupper()
name ="aamani"
print(name.isupper())

#isalnum()
#syntax:variable.isalnum()
a ="Aamani123"
print(name.isalnum())

#isdecimal()
#syntax:variable.isdecimal()
n="197998"
print(n.isdecimal())

#isassci()
#syntax:variable.isascii()
A ="123A@"
print(a.isascii())

#isspace()
#syntax:variable.isspace()
name ="Aamani Maruboina"
print(name.isspace())

name=" "
print(name.isspace())

#istitle()
#syntax:variable.istitle()
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

lst= "I Like Python"
print(lst.istitle())

#isprintable()
#syntax:variable.isprintable()
x="Hi, my name is Aamani123,!#"
print(x.isprintable())

#isidentifier()
#syntax:variable.isidentifier()
x="Aamani"
print(x.isidentifier())

n="Aamai@"
print(n.isidentifier())

#String Search Functions

#index
#syntax:variableName.index(string/char)

email="aamani@gmail.com"
print(email.index("@"))

#rindex
#syntax:variableName.rindex(string/char)

email="aamani@gmail@.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)

email="aamani@gmail@.com"
print(email.rindex("@"))

#startswith
#syntax:variableName.startswith(string/char)

name="Aamani Maruboina"
print(name.startswith("Aamani"))

#endswith
#syntax:variableName.endswith(string/char)

name="Aamani Maruboina"
print(name.endswith("Maruboina"))


#list methods

#Append
#syntax:lst.append()

l=[]
print(l.append("Aamani"))
print(l)

#insert
#syntax:lst.insert(index,item)

l=["Aamani","Anji"]
print(l.insert(1,"Sujatha"))
print(l)

#Extend
#syntax:lst.extend(lst1)

name=["Aamani","Anji"]
name1=["Anji","Sujatha"]
name.extend(name1)
print(name)

#count
#syntax:lst.count(item)

name=["Aamani","Anji","Aamani"]
print(name.count("Aamani"))

#index
#syntax:lst.index(item)

name=["Aamani","Anji"]
print(name.count("Aamani"))

#pop
#syntax:lst.pop()

name=["Aamani","Anji","Sujatha"]
print(name.pop())

#remove
#syntax:lst.remove()

name=["Aamani","Anji"]
print(name.remove("Aamani"))
print(name)

#clear
#syntax:lst.clear(item)

name=["Aamani","Anji","Sujatha"]
print(name.clear())
print(name)

#sort
#syntax:lst.sort()

a=[1,2,5,3]
a.sort()
print(a)

#reverse
#syntax:lst.reverse()

a=[1,2,5,3]
a.reverse()
print(a)


#Tuple Methods

#count
#syntax:tpl.count(item)

tpl=tuple((1,4,3,5,4))
print(tpl.count(4))

#index
#syntax:tpl.index(item)

tpl=tuple((1,2,3,))
print(tpl.index(1))

#set methods

#add
#syntax:variable.add()

a={'a','v','s'}
a.add('y')
print(a)

#update
#syntax:variable.update(setvariable)

a={'a','b','c'}
b={'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)

a={'a','b','c'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)

a={'a','b','c'}
a.discard('c')
print(a)

#pop
#syntax:variableName.pop()

a={'a','b','c'}
a.pop()
print(a)


#frozenset methods

#union
#syntax:variableName.union(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection(b))

#intersection update
#yntax:set1.intersection_update

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)

a={'a'}
b={'b'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issuperset(b))










#