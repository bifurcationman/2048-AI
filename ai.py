from board import board
import copy
import time
import math

###############################################
# decide - Outer Recursive Function
#
# Input:
#	b      - 2048 board
#	hf     - heuristic function
#	height - recursion height (>= 0)
# Output:
#	dir    - which direction to go
###############################################
def decide(b,hf,height):
	dir = "none"
	max = -1*float("inf")
	if height <= 0:
		print("Invalid Recursion Height (Must be > 0)!");
		return "error"
	else:
		if b.canMoveLeft():
			bnew = copy.deepcopy(b)
			val = rec(bnew.left(),hf,height-1)
			if max < val:
				dir = "left"
				max = val
		if b.canMoveRight():
			bnew = copy.deepcopy(b)
			val = rec(bnew.right(),hf,height-1)
			if max < val:
				dir = "right"
				max = val
		if b.canMoveUp():
			bnew = copy.deepcopy(b)
			val = rec(bnew.up(),hf,height-1)
			if max < val:
				dir = "up"
				max = val
		if b.canMoveDown():
			bnew = copy.deepcopy(b)
			val = rec(bnew.down(),hf,height-1)
			if max < val:
				dir = "down"
				max = val
		return dir
		

###############################################
# rec - Internal Recursive Function
#
# Input:
#	b      - 2048 board
#	hf     - heuristic function
#	height - recursion height (>= 0)
# Output:
#	res    - minimum heuristic value 
###############################################
def rec(b,hf,height):
	if height < 0:
		print("Recursion height < 0!!!");
		return -1;
	if height == 0:
		return hf(b)
	else:
		children = []
		if b.canMoveLeft():
			bnew = copy.deepcopy(b)
			children.append(bnew.left())
		if b.canMoveRight():
			bnew = copy.deepcopy(b)
			children.append(bnew.right())
		if b.canMoveUp():
			bnew = copy.deepcopy(b)
			children.append(bnew.up())
		if b.canMoveUp():
			bnew = copy.deepcopy(b)
			children.append(bnew.down())

		#bnew = copy.deepcopy(b)
		#children.append(bnew.down())

		if len(children) == 0:
			return -1*float("inf")
		else:
			return max([rec(x,hf,height-1) for x in children])

###############################################
# Empty Spaces Heuristic
#
# Input:
#	b - a 2048 board
# Output
#	res - number of empty tiles on the board
###############################################
def h1(b):
	return b.getNumempty()

###############################################
# 2 Count
#
# Input:
#	b - a 2048 board
# Output
#	res - number of twos on the board
###############################################
def h2(b):
	count = b.toList().count(2)
	if count == 0:
		return float("inf")
	else:
		return 1/count		

###############################################
# Sum of Squares
#
# Input:
#	b - a 2048 board
# Output
#	res - sum of the squares of the entries
###############################################
def h3(b):
	return sum([x^2 for x in b.toList()])


###############################################
# Modified Sum of Squares
#
# Input:
#	b - a 2048 board
# Output
#	res - modified sum of squares of the entries
###############################################
def h4(b):
	return sum([(x-2)^2 for x in b.toList()])

###############################################
# Weighted number of empty spaces
#
# Input:
#	b - a 2048 board
# Output
#	res - Number of empty spaces times largest tile
###############################################
def h5(b):
	return b.getNumempty()**2  * max(b.toList())

###############################################
# Penalized max tile
#
# Input:
#	b - a 2048 board
# Output
#	res - Maximum tile penalized if less then 5 tiles present
###############################################
def h6(b):
	return max(b.toList()) * math.e**(b.getNumempty()-5)


###############################################
# Number of 2's w/ too few spaces penalized
#
# Input:
#	b - a 2048 board
# Output
#	res - 1/(# 2's) penalized if less than 5 tiles present
###############################################
def h7(b):
	count = (b.toList()).count(2)
	if count == 0:
		return math.e**(b.getNumempty()-5)
	else:
		return 1/(count) * math.e**(b.getNumempty()-5)

###############################################
# Number of 2's w/ too few spaces penalized
#
# Input:
#	b - a 2048 board
# Output
#	res - 1/(# 2's) penalized if less than 5 tiles present
###############################################
def h8(b):
	return sum([x^2 for x in b.toList()]) * math.e**(b.getNumempty()-5)


###############################################
# AI Body
###############################################
recursion_depth = 3
heuristic_function = h8

b = board()
while not b.gameover():
	start_time = time.time()
	dir = decide(b,heuristic_function,recursion_depth)
	if dir == "error":
		break
	elif dir == "left":
		b = b.left()
	elif dir == "right":
		b = b.right()
	elif dir == "up":
		b = b.up()
	elif dir == "down":
		b = b.down()
	elif dir == "none":
		# make an arbitrary choice
		if b.canMoveLeft():
			b = b.left()
		elif b.canMoveRight():
			b = b.right()
		elif b.canMoveUp():
			b = b.up()
		else:
			b = b.down()
	elapsed_time = time.time() - start_time
	print(b)
	print(b.getNumempty())
	print(elapsed_time)
	print()
