f = open("fifa.txt","r", encoding="UTF-8")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
lista.remove(lista[0])
f.close()
#3.feladat.
print(f"3.feladat: {len(lista)}csapat szerepel")
#4.feladat.
p2v = lambda x: x.replace(".", ",")
pontszam = []
for sor in lista:
    pontszam.append(int(sor[-1]))
print(f"4.feladat: A csapatok átlagos pontszáma:{sum(pontszam) / len(lista):.2f} pont")
#5.feladat.

nagyobb = ""
for sor in lista:
    if nagyobb < sor[2]:
        nagyobb = sor[2]
        helyezes = sor[1]
        csapat = sor[0]
        pontszam = sor[-1]
print(f"5.feladat: a legtöbbet javító csapat:")
        
print(f"       Helyezés:{helyezes}")
print(f"       Csapat:{csapat}")
print(f"       Pontszám:{pontszam}")
#6.feladat.
if sor[0] == "Magyarország":
    print(f"A csapatok között van Magyarország")
elif sor[0] != "Magyarország":
    print(f"A csapatok között nincs magyarország.")
#7.feladat.
stat = dict()
for sor in lista:
    javitas = sor[2]
    stat[javitas] = stat.get(javitas,0) + 1
print(f"7.feladat: statisztika:")
for sor in stat.items():
    if sor[0] == "0":
        print(f"        0 helyet változott: {sor[1]} csapat")
    if sor[0] == "-1":
        print(f"       -1 helyet változott: {sor[1]} csapat")
    if sor[0] == "1":
        print(f"        1 helyet változott: {sor[1]} csapat")
    
    