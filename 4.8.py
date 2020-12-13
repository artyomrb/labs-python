ralph_waldo_emerson = """These are the voices which we hear in solitude, but they grow faint and inaudible as we enter into the world. Society everywhere is in conspiracy against the manhood of every one of its members. Society is a joint-stock company, in which the members agree, for the better securing of his bread to each shareholder, to surrender the liberty and culture of the eater. The virtue in most request is conformity. Self-reliance is its aversion. It loves not realities and creators, but names and customs."""
d = {}
for i in ralph_waldo_emerson.split(' '):
    i = i.strip('.,')
    if i: 
        d[i] = d.get(i, 0) + 1
print(d)
