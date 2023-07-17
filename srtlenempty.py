s=input("enter string:")
s.split()
if len(s)>1:
    print(s[0:2]+s[-2:])
else:
    print("Enter string...!")