import numpy

def print_stack(stack):	
	space = numpy.zeros((5,5))
	for int in stack:
		space[int[0],int[1]] = 1
	print space
	
stack = [[1,1],[2,2],[3,3]]
print_stack(stack)
	
	
def next_steps(stack):
	potential = []
	potential.append([stack[-1][0]+1,stack[-1][1]])
	potential.append([stack[-1][0]-1,stack[-1][1]])
	potential.append([stack[-1][0],stack[-1][1]+1])
	potential.append([stack[-1][0],stack[-1][1]-1])
	print_stack(potential)
	

	
next_steps(stack)
