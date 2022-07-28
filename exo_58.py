def carac_esp(chaine):
    count=0
    for i in chaine:
        if i==" ":
            count+=1
    return " "*count+("".join(chaine.split()))

print(carac_esp("La vie est belle"))