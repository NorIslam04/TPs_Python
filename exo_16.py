liste=[1,2,3,4,5]

while True:
    print(liste)
    index=int(input("Entrer un index (-1 pour quitter): "))
    if index==-1:
        print("Programme Termine!")
        print(liste)
        break
    value=int(input("Entrez une nouvelle valeur: "))
    if 0<=index<len(liste) :
        liste[index-1]=value
    else:
        liste.append(value)