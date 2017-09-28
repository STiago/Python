a = [1,2,3,4,5,6]
b = [1,5,6,7,8]

notrepeated = []
intersection = []

c = a+b

for i in c:
    if i not in notrepeated:
        notrepeated.append(i)
    else:
        if i not in intersection:
            intersection.append(i)

print intersection
