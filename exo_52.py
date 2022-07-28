from itertools import product
def repeat(chaine,ent):
    var=list(chaine)
    result=[]
    for i in product(var,repeat=ent):
         result.append(i)
    return result

print(repeat("abc",3))
