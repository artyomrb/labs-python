s = [11, 2, 5, 5, 9, 11, 8]
z = {}
for i in s:
	if i in z:
		z[i] += 1
		print (i)
	else:
		z[i] = 1
