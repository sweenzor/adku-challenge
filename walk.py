import numpy

space = numpy.zeros((5,5))
#space[0,0] = 1
locationstack = [[0,0]]

for coordinate in locationstack:
	space[coordinate[0], coordinate[1]] = 1


def moves(stack):
	current_coordinate = stack[-1]
	new[0] = current_coordinate[0] + 1
	new[1] = current_coordinate[1] + 1
	stack.append(new)

moves(locationstack)
	
#def move_up:
	

print space