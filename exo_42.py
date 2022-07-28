from collections import Counter
chaine='thequickbrownfoxjumpsoverthelazydog'
comp=Counter(chaine)
for i in comp:
    if comp[i]>=2:
        print(i,comp[i])