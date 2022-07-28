from collections import OrderedDict
def remove_duplicate(chaine):
    return "".join(OrderedDict.fromkeys(chaine))

print(remove_duplicate("python exercises practice"))