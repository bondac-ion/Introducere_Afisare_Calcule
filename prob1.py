"""De la tastatura se introduce numarul de rand al culorii curcubeului.
De afisat denumirea culorii.Convenim ca culoarea rosii are numarul de rind 1"""
n=int(input("dati numarul culorii:"))
if n==1 :
    print("rosu")
if n==2:
    print("oranj")
if n==3:
    print("galben")
if n==4:
    print("verde")
if n==5:
    print("albastru")
if n==6:
    print("indigo")
if n==7:
    print("violet")
if (n>7) or (n<1):
    print("error occured")