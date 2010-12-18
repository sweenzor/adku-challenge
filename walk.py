import numpy

def print_stack(stack,num):	
	space = numpy.zeros((5,5))
	for int in stack:
		space[int[0],int[1]] = num
	print space
	
stack = [[1,1],[4,2],[4,3]]
print_stack(stack,1)
	
	
def next_steps(stack):
	potential = []
	potential.append([stack[-1][0]+1,stack[-1][1]])
	potential.append([stack[-1][0]-1,stack[-1][1]])
	potential.append([stack[-1][0],stack[-1][1]+1])
	potential.append([stack[-1][0],stack[-1][1]-1])
	
	for next_step in potential:
		if next_step[0] < 0: potential.remove(next_step)
		if next_step[0] > 4: potential.remove(next_step)
		if next_step[1] < 0: potential.remove(next_step)
		if next_step[1] > 4: potential.remove(next_step)
		for step in stack:
			if next_step == step: potential.remove(next_step)
	
	print_stack(potential,2)
		
next_steps(stack)
