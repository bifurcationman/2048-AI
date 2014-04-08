import random

class board:
	def __init__(self):
		self.__arr = [0 for i in range(16)]
		self.__numempty = 16
		self.__max = 0
		self.spawn()
		self.spawn()

	def spawn(self):
		if self.__numempty > 1:
			r = random.randrange(0,self.__numempty-1)
		else:
			r = 0
		empty = [i for i in range(16) if self.__arr[i]==0]
		num = 4 if random.random()>=0.9 else 2
		if num > self.__max:
			self.__max = num
		self.__arr[empty[r]] = num
		self.__numempty -= 1
	
	def getNumempty(self):
		return self.__numempty

	def gameover(self):
		return not (self.canMoveLeft() or self.canMoveRight() or self.canMoveUp() or self.canMoveDown())
	
	def canMoveRight(self):
		for i in range(4):
			for j in range(3):
				me = self.__arr[4*i+j]
				nbr = self.__arr[4*i+j+1]
				if me !=0 and (me == nbr or nbr == 0):
					return True
		return False

	def canMoveLeft(self):
		for i in range(4):
			for j in range(3,0,-1):
				me = self.__arr[4*i+j]
				nbr = self.__arr[4*i+j-1]
				if me !=0 and (me == nbr or nbr == 0):
					return True
		return False

	def canMoveUp(self):
		for j in range(4):
			for i in range(3,0,-1):
				me = self.__arr[4*i+j]
				nbr = self.__arr[4*(i-1)+j]
				if me !=0 and (me == nbr or nbr == 0):
					return True
		return False

	def canMoveDown(self):
		for j in range(4):
			for i in range(3):
				me = self.__arr[4*i+j]
				nbr = self.__arr[4*(i+1)+j]
				if me !=0 and (me == nbr or nbr == 0):
					return True
		return False

	def left(self):
		for i in range(4):
			# shift left
			j = 0
			while j < 4 :
				val = self.__arr[4*i+j]
				if val == 0 or j == 0:
					j += 1
				elif j > 0 and val != 0 and self.__arr[4*i+j-1] == 0:
					self.__arr[4*i+j-1] = val
					self.__arr[4*i+j] = 0
					j -= 1
				else:
					j += 1
			# combine
			for j in range(3):
				if self.__arr[4*i+j] > 0 and self.__arr[4*i+j] == self.__arr[4*i+j+1]:
					self.__arr[4*i+j] *= 2
					self.__arr[4*i+j+1] = 0
					self.__numempty += 1
					if self.__max < self.__arr[4*i+j]:
						self.__max = self.__arr[4*i+j]
					
			# shift left
			j = 0
			while j < 4 :
				val = self.__arr[4*i+j]
				if val == 0 or j == 0:
					j += 1
				elif j > 0 and val != 0 and self.__arr[4*i+j-1] == 0:
					self.__arr[4*i+j-1] = val
					self.__arr[4*i+j] = 0
					j -= 1
				else:
					j += 1
		#spawn new tile
		self.spawn()
		return self

	def right(self):
		for i in range(4):
			# shift right
			j = 3
			while j > -1 :
				val = self.__arr[4*i+j]
				if val == 0 or j == 3:
					j -= 1
				elif j < 3 and val != 0 and self.__arr[4*i+j+1] == 0:
					self.__arr[4*i+j+1] = val
					self.__arr[4*i+j] = 0
					j += 1
				else:
					j -= 1
			# combine
			for j in range(3,0,-1):
				if self.__arr[4*i+j] > 0 and self.__arr[4*i+j] == self.__arr[4*i+j-1]:
					self.__arr[4*i+j] *= 2
					self.__arr[4*i+j-1] = 0
					self.__numempty += 1
					if self.__max < self.__arr[4*i+j]:
						self.__max = self.__arr[4*i+j]
			# shift right
			j = 3
			while j > -1 :
				val = self.__arr[4*i+j]
				if val == 0 or j == 3:
					j -= 1
				elif j < 3 and val != 0 and self.__arr[4*i+j+1] == 0:
					self.__arr[4*i+j+1] = val
					self.__arr[4*i+j] = 0
					j += 1
				else:
					j -= 1
		self.spawn()
		return self

	def up(self):
		for j in range(4):
			# shift up
			i = 0
			while i < 4 :
				val = self.__arr[4*i+j]
				if val == 0 or i == 0:
					i += 1
				elif i > 0 and val != 0 and self.__arr[4*(i-1)+j] == 0:
					self.__arr[4*(i-1)+j] = val
					self.__arr[4*i+j] = 0
					i -= 1
				else:
					i += 1
			# combine
			for i in range(3):
				if self.__arr[4*i+j] > 0 and self.__arr[4*i+j] == self.__arr[4*(i+1)+j]:
					self.__arr[4*i+j] *= 2
					self.__arr[4*(i+1)+j] = 0
					self.__numempty += 1
					if self.__max < self.__arr[4*i+j]:
						self.__max = self.__arr[4*i+j]
			# shift up
			i = 0
			while i < 4 :
				val = self.__arr[4*i+j]
				if val == 0 or i == 0:
					i += 1
				elif i > 0 and val != 0 and self.__arr[4*(i-1)+j] == 0:
					self.__arr[4*(i-1)+j] = val
					self.__arr[4*i+j] = 0
					i -= 1
				else:
					i += 1
		self.spawn()
		return self

	def down(self):
		for j in range(4):
			# shift down
			i = 3
			while i > -1 :
				val = self.__arr[4*i+j]
				if val == 0 or i == 3:
					i -= 1
				elif i < 3 and val != 0 and self.__arr[4*(i+1)+j] == 0:
					self.__arr[4*(i+1)+j] = val
					self.__arr[4*i+j] = 0
					i += 1
				else:
					i -= 1
			# combine
			for i in range(3,0,-1):
				if self.__arr[4*i+j] > 0 and self.__arr[4*i+j] == self.__arr[4*(i-1)+j]:
					self.__arr[4*i+j] *= 2
					self.__arr[4*(i-1)+j] = 0
					self.__numempty += 1
					if self.__max < self.__arr[4*i+j]:
						self.__max = self.__arr[4*i+j]
			# shift down
			i = 3
			while i > -1 :
				val = self.__arr[4*i+j]
				if val == 0 or i == 3:
					i -= 1
				elif i < 3 and val != 0 and self.__arr[4*(i+1)+j] == 0:
					self.__arr[4*(i+1)+j] = val
					self.__arr[4*i+j] = 0
					i += 1
				else:
					i -= 1
		self.spawn()
		return self
	
	def toList(self):
		return self.__arr

	def __str__(self):
		s = "%*d %*d %*d %*d \n%*d %*d %*d %*d \n%*d %*d %*d %*d \n%*d %*d %*d %*d" % tuple([item for list in zip([len(str(self.__max))]*16,self.__arr) for item in list])
		return s
