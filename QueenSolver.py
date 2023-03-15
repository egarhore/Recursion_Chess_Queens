def queen_solver(r, c, g, b_size):
	# Check rows
	i = r
	j = c
	while j >= 0:
		j -= 1
		if g[i][j] != 0:
			return 0

	# Check diagonally downwards
	i = r
	j = c
	while i >= 0 and j >= 0:
		i -= 1
		j -= 1
		if g[i][j] != 0:
			return 0

	# Check diagonally upwards
	i = r
	j = c
	while i < b_size-1 and j >= 0:
		i += 1
		j -= 1
		if g[i][j] != 0:
			return 0

	# Since possible
	g[r][c] = 1
	if c == b_size-1:
		return 1

	# Perform recursion to solve the puzzle
	for k in range(b_size):
		if queen_solver(k, c + 1, g, b_size):
			return 1
	
	# No solution
	g[r][c] = 0
	return 0
