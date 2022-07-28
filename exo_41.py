def strip_chars(str,chars):
    return ''.join(c for c in str if c not in chars)

chaine="La vie est belle .Ma vie d'antan"
print(strip_chars(chaine,"e"))