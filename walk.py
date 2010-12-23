import numpy
import os

grid_size = [3,3]

def print_stack(stack):	
	space = numpy.zeros((grid_size[0],grid_size[1]))
	for int in stack:
		space[int[0],int[1]] = stack.index(int)+1
	print space
	

	
def next_steps(stack):
	potential = []
	potential.append([stack[-1][0]+1,stack[-1][1]])
	potential.append([stack[-1][0]-1,stack[-1][1]])
	potential.append([stack[-1][0],stack[-1][1]+1])
	potential.append([stack[-1][0],stack[-1][1]-1])

	for next_step in potential[:]:
		for step in stack:
			if next_step == step: potential.remove(next_step)
		if next_step[0] < 0: potential.remove(next_step)
		if next_step[0] > grid_size[0]-1: potential.remove(next_step)
		if next_step[1] < 0: potential.remove(next_step)
		if next_step[1] > grid_size[1]-1: potential.remove(next_step)

	return potential


paths = [[[0,0],[0,1]],[[0,0],[1,0]]]

complete = []


while True:
	steps = paths.pop(0)
	new_steps = next_steps(steps)
	if new_steps:
		for step in new_steps:
			if step == [grid_size[0]-1,grid_size[1]-1]:
				complete.append(steps+[step])
				#print_stack(complete[-1])
			else:
				paths.append(steps+[step])
				#print_stack(paths[-1])
	if not paths:
		break
	if complete:
		os.system('cls')
		print print_stack(complete[-1])
	print 'last: ',paths[-1][-1]
	print 'complete: ',len(complete)
	print 'potential: ',len(paths)
	print '\n'


print '\n\n\n'

fid = open('paths.dat', 'w')
for line in complete:
	fid.write(str(line)+'\n')

print 'complete: ',len(complete)
print 'potential: ',len(paths)