chaine="32.054,23"
a=chaine.replace(".",'$')
b=a.replace(",",'%')
new=b.replace("$",",")
new2=new.replace("%",'.')
print(new2)

maketrans=chaine.maketrans
chaine=chaine.translate(maketrans(',.','.,'))
print(chaine)