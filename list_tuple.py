#Append
lst = ["Aamani","Anji","sujatha"]
lst.append("kondaiah")
print(lst)

#insert
lst = ["Aamani","anji","sujatha"]
lst.insert(1,"kondaiah")
print(lst)

#count()
lst = ["Aamani","anji","kondaiah","Aamani"]
print(lst.count("Aamani"))

attendess =["navya","vamsi","prasad","vamsi"]
if(attendess.count("bablu")>0):
    print(attendess.index("bablu"))

#update()
names = ["anji","aamani","sujatha"]
names[1]="maruboina aamani"
print(names)

#extend()
names =["aamani","anji","sujatha"]
names1 =["haritha","ananyasri"]
names.extend(names1)
print(names)
print(names1)

#delete
#remove()
names = ["aamani","teja","anji"]
names.remove("anji")
print(names)

#pop with index
names = ["aamani","teja","anji"]
names.pop(1)
print(names)

#pop without index
names=["aamani","anji","teja","haritha"]
names.pop()
print(names)

#clear
names =["aamani","anji","teja","haritha"]
names.clear()
print(names)

#delete
names = ["aamani","anji","teja","haritha"]
del names[1]
print(names)
"""
name1 =input("enter name:")
name2 =input("enter name:")
name3 =input("enter name:")
names=[]
names.append(name1)
names.append(name2)
names.append(name3)
print(names)
"""

#sort ascending order
lst = [2,3,6,1,0,7]
lst.sort()
print(lst)

#sort descending order
lst = [2,4,5,7,1,9,0]
lst.sort(reverse=True)
print(lst)

#reverse()
lst = [1,2,3,5,6,9]
lst.reverse()
print(lst)

#tuple-implicit
tpl=(1,2,3,4)
print(type(tpl))

#tuple-explicit
tpl =tuple((1,2,3,4))
print(type(tpl))

#tuple-data type/variable Annotation
tpl : tuple =(1,2,3,4)
print(type(tpl))

#tuple-count
tpl = tuple((1,2,3,4))
print(tpl.count(1))

#tuple-index
tpl =tuple((1,2,3,4))
print(tpl.index(4))

