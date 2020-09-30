"""Mariuca tine evidenta iepurilor din crescatorie.Ea isi noteaza cati iepuri sunt la inceputul lunii,
cati au murit si cati s-au nascut in cursul fiecarii luni.Puteti sa realizati un program care, primind aceste date,
sa se afiseze la sfarsitul fiecarii luni cati iepuri sumt in crescatorie"""
n_initial=int(input("nr. de iepuri la inceputul lunii:"))
m=int(input("nr. de iepuri morti:"))
n=int(input("nr. de iepuri nascuti:"))
print("la sfarsitul lunii au ramas",n_initial+n-m,"iepuri")