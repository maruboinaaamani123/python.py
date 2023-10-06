#string Operator overloading:
Fname = "Aamani"
Lname = "Maruboina"
print(Fname + " " + Lname)

fname = "prasanna"
lname = "Anjineyulu"
print(fname+" "+lname)
print("fullname:"+fname+" "+lname)

#F' string interpolation:
Fname ="Aamani"
Lname ="maruboina"
fullname=f"{Fname} {Lname}"
print(fullname)
print(f"fullname:{Fname} {Lname}")

#string join method
fname ="Sujatha"
lname ="kondaiah"
lst =(fname,lname)
print(" ".join(lst))
print("fullname:",fname,lname)

#string split
email="aamani2023@gmail.com"
print(email.split("@"))

#split lines
address:str=""" 1-34
    bcd colony
    bcd nagar
    ulavapadu(m.d)
    prakasa(d.t)
"""
print(address.splitlines())

#string partition
email="a@aamani@gmail.com"
print(email.partition("@"))

#rpartition
email="a@aamani2023@gmail.com"
print(email.rpartition("@"))









