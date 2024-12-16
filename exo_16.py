liste=[1,2,3,4,5]

while True:
    print(liste)
    index=int(input("Entrer un index (-1 pour quitter): "))
    if index==-1:
        print("Programme Termine!")
        print(liste)
        break
    value=int(input("Entrez une nouvelle valeur: "))
    #si il veut modifier un element existe deja dans la liste
    if 0<=index<len(liste) :
        liste[index-1]=value
    else:#si il veut ajouter un element a la liste a la fin
        liste.append(value)