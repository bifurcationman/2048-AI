from board import board

first = board()
while not first.gameover():
	print(first,"\n")
	print(first.getNumempty())
	print("Enter your next move : ",end="")
	move = input().strip()
	if move == 'u':
		if first.canMoveUp():
			first = first.up()
		else:
			print("**** You cannot move up! ****");
	elif move == 'd':
		if first.canMoveDown():
			first = first.down()
		else:
			print("**** You cannot move down! ****");
	elif move == 'l':
		if first.canMoveLeft():
			first = first.left()
		else:
			print("**** You cannot move left! ****");
	elif move == 'r':
		if first.canMoveRight():
			first = first.right()
		else:
			print("**** You cannot move right! ****");
print("\n\n Game Over \n\n")
