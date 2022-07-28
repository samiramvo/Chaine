chaine="La vie est belle"
def no_repeat(chaine):
    liste=[]
    ctr={}
    for i in chaine:
        if i in ctr:
            ctr[i]+=1
            liste.append(i)
    for c in liste:
        if ctr[c]==1:
            return c
    return None

print(no_repeat(chaine)) 