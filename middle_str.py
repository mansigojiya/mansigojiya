"""a=input("enter name:-")

if len(a):
    print(a[:2] +'rajesh'+a[2:])
else:
    print("sorry...!")"""
def mstr(str,word):
    print("String:-",str)
    print("Second String:-",word)
    print(str[:2]+ word +str[2:])

s1=input("Enter String:-")
s2=input("Enter Second String:-")
mstr(s1,s2)