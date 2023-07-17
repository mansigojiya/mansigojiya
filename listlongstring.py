data=list()

n=int(input("Enter number of value:-"))

for i in range(n):
    x=input("Enter your data:-")
    data.append(x)
#print(data)
for d in data:
    print(d)
a=len(data[0])
b=data[0]
for i in data:
    if(len(i)>a):
        a=len(i)
        b=i
print("The lngest length word is:-",b," ","\n length is:-",a)