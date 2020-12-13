ralph_waldo_emerson = """These are the voices which we hear in solitude but they grow faint and inaudible as we enter into the world Society everywhere is in conspiracy against the manhood of every one of its members Society is a joint-stock company in which the members agree for the better securing of his bread to each shareholder to surrender the liberty and culture of the eater The virtue in most request is conformity Self-reliance is its aversion It loves not realities and creators but names and customs"""
words_emerson = list(map(str.lower,ralph_waldo_emerson.split()))
 
def sorted_string(s):
    return ''.join(sorted(s))
 
anagram = {}
for i in words_emerson:
    word = sorted_string(i)
    anagram.setdefault(word,[])
    anagram[word].append(i)
 
for w,a in anagram.items():
    print(*a)
