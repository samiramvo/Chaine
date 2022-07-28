from re import A


chaine="La vie est belle"
def inverse_lett(chaine):
    a=chaine[0]
    chaine[0]=chaine[-1]
    chaine[-1]=a
    return chaine

print(inverse_lett(chaine))