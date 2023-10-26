#general function

def add():
    a=5
    b=10
    print(a+b)
add()

def sub():
    a=5
    b=10
    print(a-b)
sub()

def div():
    a=10
    b=20
    print(a/b)
div()

def mul():
    a=10
    b=20
    print(a*b)
mul()

#armstrong number
def armstrong():
    n = (input("enter any number"))
    m = int(n)
    sum = 0
    while (m > 0):
        r = m % 10
        sum = sum + r ** len(n)
        m = m // 10
    if (int(n) == sum):
        print("it is a Armstrong Number")
    else:
        print("it is a not Armstorng Number")
armstrong()

#even numbers
def even():
    n = int(input("enter number"))
    if (n % 2 == 0):
        print("given number is even")
    else:
        print("given number is not even")
even()

#palindrome number
def palindrome():
    n = int(input("enter a number"))
    m = n
    res = 0
    while (n > 0):
        r = n % 10
        res = res * 10 + r
        n = n // 10
    if (m == res):
        print("given number is a palindrome")
    else:
        print("given number is a not palindrome")
palindrome()

#parameterized function
def add(literal1:int,literal2 :int):
    print(literal1 + literal2)
add(10,20)

def sub(literal1 : int, literal2 : int):
    print(literal1 - literal2)
sub(10,20)

#function with named parameters
def sub(literal1:int,literal2:int):
    print(literal1 - literal2)
add(10,20)
a=10
b=20
sub(literal1=a,literal2=b)
sub(literal2=b,literal1=a)