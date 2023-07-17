a=int(input("Enter Number A:-"))
b=int(input("Enter Number B:-"))

print("A=",a)
print("B=",b)

#swaping with third var.
temp=a
a=b
b=temp
print("Value of A {}".format(a))
print("Value of B {}".format(b))

#swapping without third var

a,b=b,a
print("After A=",a)
print("After B=",b)
