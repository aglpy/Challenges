import walk_path

#This is the map example given
arr = [
[0,0,0,1,0,0],
[0,1,1,1,3,0],
[0,1,0,0,0,0],
[0,1,1,1,2,0],
[1,1,0,0,0,0]
]

print("Initial status:") #Printing initial status
print("  " + str(arr).replace(","," ").replace("[","").replace("]","\n"))

path_solved = walk_path.walk_path(arr) #Calling the path solver with the example

print("\nBest path calculated:") #Printing results
print("  " + str(arr).replace(","," ").replace("[","").replace("]","\n").replace("4","*"))
print(path_solved)