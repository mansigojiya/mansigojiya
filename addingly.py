a=input("Enetr string:-")
if len(a)>2:
    if a.endswith("ing"):
        a += 'ly'
    else:
        a +='ing'
print(a)