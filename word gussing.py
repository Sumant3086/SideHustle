Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic

# Driver code
if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = logic.start_game()

while(True):

	# taking the user input
	# for next step
	x = input("Press the command : ")

	# we have to move up
	if(x == 'W' or x == 'w'):

		# call the move_up function
		mat, flag = logic.move_up(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not over then continue
		# and add a new two
... 		if(status == 'GAME NOT OVER'):
... 			logic.add_new_2(mat)
... 
... 		# else break the loop
... 		else:
... 			break
... 
... 	# the above process should be followed
... 	# in case of each type of move
... 	# below
... 
... 	# to move down
... 	elif(x == 'S' or x == 's'):
... 		mat, flag = logic.move_down(mat)
... 		status = logic.get_current_state(mat)
... 		print(status)
... 		if(status == 'GAME NOT OVER'):
... 			logic.add_new_2(mat)
... 		else:
... 			break
... 
... 	# to move left
... 	elif(x == 'A' or x == 'a'):
... 		mat, flag = logic.move_left(mat)
... 		status = logic.get_current_state(mat)
... 		print(status)
... 		if(status == 'GAME NOT OVER'):
... 			logic.add_new_2(mat)
... 		else:
... 			break
... 
... 	# to move right
... 	elif(x == 'D' or x == 'd'):
... 		mat, flag = logic.move_right(mat)
... 		status = logic.get_current_state(mat)
... 		print(status)
... 		if(status == 'GAME NOT OVER'):
... 			logic.add_new_2(mat)
... 		else:
... 			break
... 	else:
... 		print("Invalid Key Pressed")
... 
... 	# print the matrix after each
... 	# move.
... 	print(mat)
