def permu(text):
	solucion = [] #The list to return

	for i in range(1,len(text)+1): #Index is displaced to avoid permutation of one-character text
		solucion += [text[i-1] + semi for semi in permu(text[:i-1] + text[i:])] 
		
	return solucion or text #If solution is empty, text is one character and the solution
	