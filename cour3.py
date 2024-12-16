ligne=int(input("Entrer le nombre de lignes: "))
row="*"
while ligne>0:
    print(" "* ligne + row)
    row += "**"
    ligne-=1
