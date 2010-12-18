import numpy

def print_stack(stack,num):	
	space = numpy.zeros((5,5))
	for int in stack:
		space[int[0],int[1]] = num
	print space
	

	
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

	return potential


paths = [[[0,0]]]
print_stack(paths[0],1)	


for stack in paths:	
	test = stack 
	print test
	print '\n'
	new_steps = next_steps(stack)
	for step in new_steps:
		paths.append(stack + [step])
	paths.remove(stack)
	

print paths
