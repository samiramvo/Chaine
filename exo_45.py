import re
def alphabet(chaine):
    if re.search("[A-Z]",chaine) or re.search("[a-z]",chaine):
        return True
    else:
        return False

print(alphabet("La vie est belle"))

import string
alphabet=set(string.ascii_lowercase)

chaine="The quick brown fox jumps over the lazy dog"
print(set(chaine.lower())>=alphabet)