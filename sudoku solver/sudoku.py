
from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	x=pos[0]
	y=pos[1]
	# your code goes here
	if x/3 <=1:
		if y/3<=1:
			return(1)
		elif y/3<=2:
			return(2)
		elif y/3<=3:
			return 3
	elif x/3 <=2:
		if y/3<=1:
			return(4)
		elif y/3<=2:
			return(5)
		elif y/3<=3:
			return 6
	elif x/3 <=3:
		if y/3<=1:
			return(7)
		elif y/3<=2:
			return(8)
		elif y/3<=3:
			return 9
	

	return 0

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	# your code goes here
	# c=get_block_num(sudoku, pos)#block number
	d=pos[0]%3
	e=pos[1]%3
	if d==1 and e==1:
		return(1)
	elif d==1 and e==2:
		return(2)
	elif d==1 and e==0:
		return(3)
	elif d==2 and e==1:
		return(4)
	elif d==2 and e==2:
		return(5)
	elif d==2 and e==0:
		return(6)
	elif d==3 and e==1:

		return(7)
	elif d==3 and e==2:
		return(8)
	elif d==3 and e==0:
		return(9)
		


	return 0


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	# your code goes here
	list=[]
	

	if x==1:
		for i in range(3):
			for j in range(3):

				list.append(sudoku[i][j])
	if x==2:
		for i in range(3):
			for j in range(3,6):

				list.append(sudoku[i][j])
	if x==3:
		for i in range(3):
			for j in range(6,9):

				list.append(sudoku[i][j])
	if x==4:
		for i in range(3,6):
			for j in range(3):

				list.append(sudoku[i][j])
	if x==5:
		for i in range(3,6):
			for j in range(3,6):

				list.append(sudoku[i][j])
	if x==6:
		for i in range(3,6):
			for j in range(6,9):

				list.append(sudoku[i][j])
	if x==7:
		for i in range(6,9):
			for j in range(3):

				list.append(sudoku[i][j])
	if x==8:
		for i in range(6,9):
			for j in range(3,6):

				list.append(sudoku[i][j])
	if x==9:
		for i in range(6,9):
			for j in range(6,9):

				list.append(sudoku[i][j])
				



	return list
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	list=[]
	x=i-1
	for j in range(9):

		list.append((sudoku[x][j]))
	return list

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	# your code goes here
	list=[]
	y=x-1
	for j in range(9):
		list.append(sudoku[j][y])

	return list

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here
	
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return (i+1,j+1)

	return(-1,-1)

			
	
			
	

	
def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	for i in range(8):
		if lst[i]!=0:
			for j in range(i+1,9):
				if lst[i]==lst[j]:
					return False
	return True


	

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	
	for i in range(1,10):
		if valid_list(get_row(sudoku,i)) == False or valid_list(get_column(sudoku,i)) == False or valid_list(get_block(sudoku,i)) == False:
			return(False)
	return True



def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	# your code goes here
	num=[1,2,3,4,5,6,7,8,9] 
	
	_block = get_block(sudoku,get_block_num(sudoku,pos))
	_row = get_row(sudoku, pos[0])
	_column= get_column(sudoku,pos[1])
	All_list = _block + _row + _column # A list containing all the elements of block ,  row
	#column
	list=[x for x in num if x not in All_list] # candidate is the list of element which are not in All_list
	return list

	

	

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1]=num

	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1]=0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	
	if valid_sudoku(sudoku) == False:
		return(False,sudoku)
	unass_pos= find_first_unassigned_position(sudoku)
	if unass_pos[0]== -1:
		return True,sudoku
		
	else:
		candidates= get_candidates(sudoku,unass_pos)
		if len(candidates)==0:
			return (False,sudoku)
	for i in candidates:
		make_move(sudoku,unass_pos,i)
		if sudoku_solver(sudoku)[0]==False:
			undo_move(sudoku,unass_pos)
		else:
			sudoku_solver(sudoku)
			break
	unass_pos= find_first_unassigned_position(sudoku)
	if unass_pos[0]== -1:
		return True,sudoku
	else:
		return False,sudoku 		
		# if(valid_sudoku(sudoku)):
			# 	return(True,sudoku)
			# else:
			# 	return(False,sudoku)


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

# def in_lab_component(sudoku: List[List[int]]):
	
# 	print("Testcases for In Lab evaluation")
# 	print("Get Block Number:")
# 	print(get_block_num(sudoku,(4,4)))
# 	print(get_block_num(sudoku,(1,3)))
# 	print(get_block_num(sudoku,(2,2)))
	
# 	print("Get Block:")
# 	print(get_block(sudoku,5))
# 	print(get_block(sudoku,1))
# 	print(get_block(sudoku,1))
# 	print("Get Row:")
# 	print(get_row(sudoku,4))
# 	print(get_row(sudoku,1))
# 	print(get_row(sudoku,2))
	# print("column")
	# print(get_column(sudoku,4))
	
	# print(valid_list(get_row(sudoku,9)))
	# print(find_first_unassigned_position(sudoku))
	# print(valid_sudoku(sudoku))
	# print(get_candidates(sudoku, (4,4)))
	# print(get_candidates(sudoku,(1,3)))
	# print(get_candidates(sudoku, (2,2)))
# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	#in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)