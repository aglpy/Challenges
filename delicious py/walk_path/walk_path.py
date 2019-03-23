import math

def walk_path(mapa):
	
	map_c = []
	for i in range(len(mapa)): #Copy the map to modify it
		map_c.append(mapa[i].copy())
		
	for i in range(len(map_c)): #Add wall limits to the map
		map_c[i].insert(0,0)
		map_c[i].append(0)
	map_c.insert(0,[0]*len(map_c[0]))
	map_c.append([0]*len(map_c[len(map_c)-1]))
	
	for i in range(len(map_c)): #Finding the player and exit door position
		if 2 in map_c[i]:
			door = [i,map_c[i].index(2)] #Door position
		if 3 in map_c[i]:
			player = [i,map_c[i].index(3)] #Player position
	
	tray = [] #Will get the path coordinates
	tray.append(player)
	fin = False #Player is not on exit door
	while not fin: 
		dist2_1 = math.inf #Set a square of distance to exit door on infinity
		for i in [-1,0,1]: #Test all position around player
			for j in [-1,0,1]:
				if j == 0 or i == 0: #Ignore diagonal movement
					if map_c[player[0]+i][player[1]+j] == 2: #It is exit door
						new_pos = [player[0]+i,player[1]+j] #The new position is the exit door
						fin = True #Payer is on exit door
						break
					elif map_c[player[0]+i][player[1]+j] == 1: #It isn't wall
						dist2_2 = (player[0]+i-door[0])**2+(player[1]+j-door[1])**2 #Square of distance to exit door
						if dist2_2 < dist2_1:
							new_pos = [player[0]+i,player[1]+j] #Set new position on the closest to exit door
							dist2_1 = dist2_2
			if fin: break
			
		if new_pos == player: #If new position is player position means player can't walk this way
			new_pos = tray[-2] #Go back on the path
			tray.pop() #Remove the fake way from the path
			tray.pop()
				
		tray.append(new_pos) #Add new position to the path
		map_c[player[0]][player[1]] = 0 #The old player position now is a wall :)
		map_c[new_pos[0]][new_pos[1]] = 3 #Player move to new position
		player = new_pos

	for i in range(len(tray)): #Remove limit wall coordinates
		tray[i][0] -= 1
		tray[i][1] -= 1
		
	for pos in tray: #Draw the path on the original map
		mapa[pos[0]][pos[1]] = 4
	
	return tray