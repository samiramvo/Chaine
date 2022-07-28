liste=["vert","noir","rouge"]
new=[word for word in liste.split(",")]
print(",".join(sorted(list(set(new)))))