import fit_word

arr = [
["#","#","#","#","#"],
["#","#","#","#","#"],
["#","N","O","#","#"],
["#","#","#","#","#"],
["#","#","#","#","#"]
]

word = "pot"

if fit_word.fit_word(arr, word): #Call the function and print the solution
	for fil in arr:
		print(str(fil).replace("[","").replace("]","").replace(",","").replace("'",""))
else:	
	print("It don't fit in")