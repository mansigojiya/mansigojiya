#Fibonacci sequence up to n-th term
nterms=int(input("How many terms:-"))
#first two terms
n1, n2 =0, 1
count=0

if nterms <=0:
    print("please enter a positive Number")
elif nterms==1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:-")
    while count < nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2 =nth
        count += 1