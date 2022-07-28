chaine="La vie est belle"

def supp(chaine):
    new=""
    for i in len(str(chaine)):
        if i%2==0:
            new+=i
    return chaine

print(supp(chaine))
