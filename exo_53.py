          
def carc_repeat(chaine):
    liste=[]
    for i in chaine:
        if i not in liste:
            liste.append(i)
        else:
            return i,chaine.index(i)
            break

print(carc_repeat("abcabc"))