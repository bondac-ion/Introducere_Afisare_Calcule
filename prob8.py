"""Se introduc de la tastatura trei cifre.Afisati pe aceeasi linie 5 numere
formate cu aceste cifre luate o singura data.Ex:date de intrare: 3 4 2
Date de iesire: 324 342 243 234 432"""
a=int(input("dati primul numar:"))
b=int(input("dati numarul 2:"))
c=int(input("dati numarul 3:"))
print(100*a+10*b+c,100*b+10*a+c,100*a+10*c+b,100*b+10*c+a,c*100+10*a+b,sep=" ")