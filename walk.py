import numpy

def print_stack(stack):	
	space = numpy.zeros((5,5))
	for int in stack:
		space[int[0],int[1]] = 1
	print space
	
stack = [[1,1],[2,2],[3,3]]
print_stack(stack)
