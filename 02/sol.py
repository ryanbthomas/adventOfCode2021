import day02


(d, u) = day02.load_commands("input")


print("Check to see if we can move the sub")
pos = day02.move_to_final_pos(day02.move_sub, (0, 0), d, u) 
print ("The final position is {}".format(pos))

print("Part 1 answer is {} * {} = {}".format(pos[0], pos[1], pos[0]*pos[1]))

print("Let's move the sub using correct method")
pos = day02.move_to_final_pos(day02.move_sub2, (0, 0, 0), d, u) 
print ("The final position is {}".format(pos))

print("Part 1 answer is {} * {} = {}".format(pos[0], pos[1], pos[0]*pos[1]))