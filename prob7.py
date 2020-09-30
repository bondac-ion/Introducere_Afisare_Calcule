"""Maria vrea sa verifice daca greutatea si inaltimea ei corespund virstei pe care o are.
Ea a gasit intr-o carte urmatoarele formule de calculmale greutatii si inaltimii unui copil,
v,fiind varsta:greutatea=2*v+8(in kg), inaltimea=5*v+80(in cm).Realizati un program care sa
cireasca varsta unui copil si sa afiseze greutatea si inaltimea ideala, folosind aceste formule.""" 
v=int(input("dati varsta:"))
greutatea=2*v+8
inaltimea=5*v+80
print("varianta ideala este:","greutatea",greutatea,"kg"," iar","inaltimea",inaltimea,"centimetri")