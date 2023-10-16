#curd operations
#create
lst = ["Aamani",1,True]
print(lst)

#Append()
lst :lst=["Aamani","chichu","anji"]
lst.append("ammu")
print(lst)

#insert()
attendeess=["navya","vamsi","prasad"]
attendeess.insert(4,"Aamani")
print(attendeess)

#count()
attendeess=["navya","Aamani","vamsi","prasad","Aamani"]
print(attendeess.count("Aamani"))
print(attendeess.count("abc"))

#index().
attendeess=["navya","vamsi","prasad"]
print(attendeess.index("prasad"))

#count()
attendeess = ["navya","vamsi","prasad","vamsi"]
if(attendeess.count("bablu")<0):
    print(attendeess.index("bablu"))

#update by using index
attendeess=["navya","vamsi","prasad"]
attendeess[1]= "Mohan vamsi"
print(attendeess)

#extend
attendeess=["navya","vamsi","prasad"]
attendeess1=["Aamani"]
attendeess.extend(attendeess1)
print(attendeess)

#delete
attendeess=["navya","vamsi","prasad"]
attendeess.remove("prasad")
print(attendeess)

attendeess=["navya","vamsi","prasad"]
attendeess.remove("navya")
print(attendeess)

#pop with index
attendeess=["navya","vamsi","prasad"]
attendeess.pop(2)
print(attendeess)

#pop without index
attendeess=["navya","vamsi","prasad"]
attendeess.pop()
print(attendeess)