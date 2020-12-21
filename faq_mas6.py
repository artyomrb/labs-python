s = [11, 2, 5, 5, 9, 11, 8]
z = set()
m = []
for i in s:
	if i in z:
		continue
	z.add(i)
	m.append(i)
print(m)
