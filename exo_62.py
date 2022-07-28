
def somme_numb(chaine):
    som=0
    for i in chaine:
        if i.isdigit==True:
            z=int(i)
            som+=z
    return som

print(somme_numb("123abcd45"))