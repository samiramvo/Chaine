def lexico_sort(chaine):
    return sorted(sorted(chaine),key=str.upper)

print(lexico_sort('w3ressource'))