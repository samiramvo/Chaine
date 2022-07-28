def renvoie(chaine):
    if len(chaine)<2:
        return []
    else:
      return(chaine[0]+chaine[1]+chaine[-2]+chaine[-1])

print(renvoie("lavieestbelle"))