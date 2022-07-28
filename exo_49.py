def vowels(chaine):
    som=0
    liste=[]
    vowels="aeiouAEIOU"
    for i in chaine:
        if i in vowels:
            liste.append(i)
            som+=1
    return som,liste
   

print(vowels('w3resource'))