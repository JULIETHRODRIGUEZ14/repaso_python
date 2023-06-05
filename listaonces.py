onces=["combo", "sandwich", "pizza"]
onces.insert(2, "empanada")
onces.append("gaseosa")
onces.extend(["malteada","perro caliente"])
onces.remove("malteada")
del onces[0]
onces.pop()
onces.sort();
#onces.reverse();
onces.sort(reverse=True);

print(onces)