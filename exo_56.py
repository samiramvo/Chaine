chaine ="La vie de louga. La vie des riches"
def mot_repeat(chaine):
    liste=[]
    count=0
    chaine=chaine.split()
    for i in chaine:
        if i in liste:
            count+=1
            if count==2:
              return i,chaine.index(i)
        else:
            liste.append(i)
    return "None"
    
print(mot_repeat(chaine))


