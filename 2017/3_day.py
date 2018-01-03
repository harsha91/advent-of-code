import math

print("Advent of Code - DAY 3")

''' 
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
'''

def createSpiral(input):
	i = x = y = 0;
	spiral = {}
	# 1R, 1U, 2L, 2D one cycle
	# inc of 2
	# start with 6, inc of number is 8 
	toNumber = 7 
	incNumber = 8
	n = 0
	rM = uM = 1
	lM = dM = 2
	while i < input :
		if i == 0:
			spiral[i] = ([x, y])
			i = i + 1
		else:
			for k in range(n + rM):
				y = y + 1
				spiral[i] = ([x, y])
				i = i + 1
			for k in range(n + uM):
				x = x + 1
				spiral[i] = ([x, y])
				i = i + 1
			for k in range(n + lM):
				y = y - 1
				spiral[i] = ([x, y])
				i = i + 1
			for j in range(n + dM):
				x = x - 1
				spiral[i] = ([x, y])
				i = i + 1
			n = n + 2	
	print("Input  is " + str(input) + " coordinates " + str(spiral[input-1]))
	return spiral[input-1]

def createSpiral2(input):
	i = x = y = 0;
	size = int(math.ceil(math.sqrt(input)))
	spiral = {}
	# 1R, 1U, 2L, 2D one cycle
	# inc of 2
	# start with 6, inc of number is 8 
	toNumber = 7 
	incNumber = 8
	n = 0
	rM = uM = 1
	lM = dM = 2
	try:
		while i < input :
			if i == 0:
				spiral[(x,y)]=1
				i = i + 1
			else:
				for k in range(n + rM):
					y = y + 1
					spiral[(x,y)] = getNeighborsSum(spiral, x, y, i, input)
					i = i + 1
				for k in range(n + uM):
					x = x + 1
					spiral[(x,y)] = getNeighborsSum(spiral, x, y, i, input)
					i = i + 1
				for k in range(n + lM):
					y = y - 1
					spiral[(x,y)] = getNeighborsSum(spiral, x, y, i, input)
					i = i + 1
				for j in range(n + dM):
					x = x - 1
					spiral[(x,y)] = getNeighborsSum(spiral, x, y, i, input)
					i = i + 1
				n = n + 2	
	except ValueError as error:
		print(str(error))


def getNeighborsSum(spiral, x , y, index, input):
	sum = 0
	sum = sum + spiral.get((x+1, y), 0)
	sum = sum + spiral.get((x-1, y), 0)
	sum = sum + spiral.get((x, y+1), 0)
	sum = sum + spiral.get((x, y-1), 0)
	sum = sum + spiral.get((x+1, y+1), 0)
	sum = sum + spiral.get((x+1, y-1), 0)
	sum = sum + spiral.get((x-1, y-1), 0)
	sum = sum + spiral.get((x-1, y+1), 0)
	if sum > input:
		raise ValueError('YAY the value is ' + str(sum))
	return sum


def calculateDist(coordinates):
	return math.fabs(coordinates[0]-0)+math.fabs(coordinates[1]-0)

if __name__ == '__main__':
	input = 265149
	coordinates = createSpiral(input)
	print ("Manhattan dist is " + str(calculateDist(coordinates)))
	createSpiral2(input)

'''
37	36	35	34	33	32	31
38	17  16  15  14  13	30
39	18   5   4   3  12	29
40	19   6   1   2  11	28	
41	20   7   8   9  10	27	
42	21  22  23	24	25	26
43	44	45	46	47	48	49
'''