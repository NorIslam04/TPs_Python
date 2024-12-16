nbr=int(input("nombre: "))
i=1
j=1

while i<=nbr:
    j=0
    while j<=nbr:
        if i*j==nbr:
            print(i,"*",j,"= ",j*i)
        j+=1
    i+=1        