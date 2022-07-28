liste=['Sami','Exercises','Dimanche','Filer']
liste_len=[]
for i in liste:
    liste_len.append((len(i),i))

liste_len.sort()
print(liste_len[-1])
