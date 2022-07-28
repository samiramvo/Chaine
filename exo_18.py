mot=input("Entrez un mot mot: ")
def mot_end(mot):
    if len(mot)>=3:
      return (mot[0]+mot[1]+mot[2])
    else:
        return mot

print(mot_end(mot))