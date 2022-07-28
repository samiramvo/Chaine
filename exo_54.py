def first_repeat(chaine):
    temp={}
    for i in chaine:
        if i in temp:
            return i,chaine.index(i)
        else:
            temp[i]=0
    return 'None'

print(first_repeat("abcabc"))