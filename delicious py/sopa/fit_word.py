def fit_word(sopa, pal):
	lpal = list(pal.upper()) #Convert the word into list
	posi = [] #New matrix to unify rows and colums in just rows
	
	for fil in sopa: #Unify rows and columns in a new matrix as rows
		posi.append(fil)
	for icol in range(len(sopa[0])):
		posi.append([sopa[i][icol] for i in range(len(sopa))])
		
	best = [None, None] #Will get the best solution coordinates
	count = -1
	coin_1 = 0
	for ele in posi: #Analyze all posible rows to fit the word
		count+=1
		for i in range(len(ele)-len(lpal) + 1): #Analyze all positions into the row to fit the word
			coin_2 = 0
			nohash = 0
			for j in range(len(lpal)): #Analyze all the characters in the word and in the sub-row
				if ele[i+j] != "#": #Save the number of no-hashes in the sub-row
					nohash+=1
				if lpal[j] == ele[i+j]: #Save the coincidences of the word and the sub-row
					coin_2+=1
			if coin_2 > coin_1 and coin_2 == nohash: #If the word fit it save the posible position
				best = [count, i] #If there is other posibility with more characters fit it will be replaced
				coin_1 = coin_2
	
	if not best[0]: #If there is no solution return False
		return False
		
	if best[0] < len(sopa): #Draw the word on the original matrix
		for i in range(len(lpal)):
			sopa[best[0]][best[1]+i] = lpal[i]
	else:
		for i in range(len(lpal)):
			sopa[best[1]+i][best[0]-len(sopa)] = lpal[i]
	return True