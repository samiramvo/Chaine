chaine ="La vie de louga. La vie des riches"
def mot_repeat(chaine):
    liste=[]
    chaine=chaine.split()
    for i in chaine:
        if i not in liste:
            liste.append(i)
        else:
            return i,chaine.index(i)
    return None
    
print(mot_repeat(chaine))


