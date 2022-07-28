def maj(chaine):
    num=0
    for lettre in chaine[:4]:
        if lettre.upper()==lettre:
            num+=1
    if num>=2:
        return chaine.upper()
    return chaine


print(maj('Python'))