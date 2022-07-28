chaine="La vie est belle"
for i in range(1,len(chaine)):
    if i==len(chaine)/2:
        chaine.insert("bonjour",len(chaine)/2)

print(str(chaine))