n=int(input("enter a number"))
m=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(m==rev):
    print("given number is a palindrome")
else:
    print("given number is a not palindrome")
