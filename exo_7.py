chaine="Les paroles ne sont pas si pauvre que ca"
for i in chaine:
  if i=='ne' or i=='pas' or i=='si'or i=='que' or i=='ca':
    del chaine(i)
print(chaine)