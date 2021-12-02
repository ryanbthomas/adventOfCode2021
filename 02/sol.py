import day02


(d, u) = day02.load_commands("input")

print("directions: {}".format(d))
print("units: {}".format(u))

print("Check to see if we can move the sub")
pos = (0, 0)
for i in range(len(d)):
    new_pos = day02.move_sub(pos, d[i], u[i])
    print("Move sub from {} {} {} units -> {}".format(pos, d[i], u[i], new_pos))        
    pos = new_pos
 
print ("The final position is {}".format(pos))

print("Part 1 answer is {} * {} = {}".format(pos[0], pos[1], pos[0]*pos[1]))