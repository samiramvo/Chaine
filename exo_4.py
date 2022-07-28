chaine="restarterrrag"
def change(chaine):
    var=chaine[0]
    chaine=chaine.replace(var,'$')
    chaine=var+chaine[1:]
    return chaine

print(change(chaine))