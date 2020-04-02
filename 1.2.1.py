objects = [1, True, 0, False]
a = set()
for i in objects:
    a.add(id(i))
print(len(a))
