n = int(input("enter number"))
if(n==0 or n==1):
    print("not a prime")
for i in range(2,n//2+1,1):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("given number a prime number")



