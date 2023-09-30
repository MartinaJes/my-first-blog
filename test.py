studenti = [
{'meno': 'Ola', 'vek': 21},
{'meno': 'Anna', 'vek': 18},
{'meno': 'Jano', 'vek': 25},
{'meno': 'Jano', 'vek': 25}

]


pocet = 0

#kolki maju viac ako 20 rokov?

for student in studenti:

    if student["vek"]>=20:
        pocet=pocet +1
print(pocet)        

for student in studenti:

    if student["meno"]=="Jano":
        print("V zozname je Jano.") 
            
     