def change(chaine):
   
    if len(chaine)>=3 and chaine[-3:]=='ing':
        return chaine+'ly'
    else:
        return chaine +'ing'
    if len(chaine)<3:
        return chaine

print(change('abc'))
print(change('string'))