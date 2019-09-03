def word_freq(s):
	s = s.replace(",","").replace(".","").replace("?","").replace("!","").replace(";","").split()
	fs = sorted(list(set([(sum(x == w for w in s), x) for x in s])), reverse=True)
	[print(f"{w}{' '*(max(len(v[1]) for v in fs)-len(w))} - frequency: {n} {n*'#'}") for n, w in fs]
