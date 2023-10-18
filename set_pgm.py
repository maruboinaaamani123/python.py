#set data type implicit
a = {'a','b','c','d'}
print(a)
print(type(a))

#explicit
a =set(('a','b','c'))
print(a)
print(type(a))

#data type/variable annotation
a : set ={'a','b','c','d'}
print(a)
print(type(a))

#set create
a : set ={'a','b','c'}
a.add('d')
print(a)

#update
a :set ={'a','b','c'}
b :set ={'b','c','d'}
a.update(b)

#remove
a:set ={'a','b','c'}
a.remove('c')
print(a)

#discard
a:set ={'a','b','c'}
a.discard('d')
print(a)

#pop
a:set =['a','b','c','d']
a.pop()
print(a)

#union
a:set={'a','b','c','d'}
b:set={'b','c','d','e'}
print(a.union(b))

#intersection
a:set={'a','b','c','d'}
b:set={'b','c','d','e'}
print(a.intersection(b))
