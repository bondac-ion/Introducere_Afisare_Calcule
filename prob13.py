"""se da o suma de bani ,de aflat suma minimala de bancnote echivalenta cu suma,
nominalul bancnotelor:1000, 500, 200, 100, 50, 20, 10, 5, 2, 1"""
n=int(input("dati o suma de bani:"))
b_1000=n//1000
b_500=(n%1000)//500
b_200=((n%1000)%500)//200
b_100=(((n%1000)%500)%200)//100
b_50=((((n%1000)%500)%200)%100)//50
b_20=(((((n%1000)%500)%200)%100)%50)//20
b_10=((((((n%1000)%500)%200)%100)%50)%20)//10
b_5=(((((((n%1000)%500)%200)%100)%50)%20)%10)//5
b_2=((((((((n%1000)%500)%200)%100)%50)%20)%10)%5)//2
b_1=(((((((((n%1000)%500)%200)%100)%50)%20)%10)%5)%2)//1
print("Va fi nevoie de urmatoarele bancnote",b_1000,"o mie;",b_500,"cinci sute;",b_200,"doua sute;",b_100,"o suta;",b_50,"cinci zeci;",b_20,"doua zeci;",b_10,"zece;",b_5,"cinci;",b_2,"doi;",b_1,"unu;")
