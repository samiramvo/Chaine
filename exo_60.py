chaine="la vie est belle"
def maj_min(chaine):
    return chaine[0].upper()+chaine[1:-1]+chaine[-1].upper()

print(maj_min(chaine))