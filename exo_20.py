from re import X


def inverser(chaine):
    if len(chaine)%4==0:
        return ''.join(reversed(chaine))
    return chaine

print(inverser("lavieestbelle"))
print(inverser("lola"))