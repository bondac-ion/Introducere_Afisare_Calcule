"""Un bradulet este impodobit cu globulete albe,rosii si albastre.Numarul globuletelor albe se citeste de la tastatura.
Cate globulete are bradutul, stiind ca numarul de globulete rosii este cu 3 mai mare decat numarul de globulete albe,
iar globulete albastre cu 2 mai putine decat totalul celor albe si rosii.Ex:Date de intrare:12;Date de iesire:52"""
n_a=int(input("nr. de globulete albe:"))
n_r=n_a+3
n_b=(n_r+n_a)-2
nt=n_a+n_b+n_r
print("pe brad sunt",nt," globulete")