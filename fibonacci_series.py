"""
n=int(input("enter number of terms"))
a=0
b=1
print(a,b,end="")
for i in range(2,n):
    c=a+b
    print(",",c,end="")
    a=b
    b=c
"""
"""
n = 10
a = 1
b = 0
i = 1
while(i <= n):
    print(b)
    a = a+b
    b = a-b
    i += 1
"""
n = 20
a = 1
b = 0
i = 1
while(i <= n):
    print(b)
    a =a+b
    b =a-b
    i +=1
