import numpy as np
import copy
import matrix_def
matrix=matrix_def.matrix

#Before starting, go to the matrix_def.py file and select which input matrix to use. I have supplied 3 of them but you can add your own custom one. Just remember, it has to a square matrix.

noofmoves=0

#This function changes all the colors of the tiles in a block
def floodfill(matrix, x, y,topleft,tochange):
	#We are changing the top left square to another color
    if matrix[x][y] == topleft:  
        matrix[x][y] = tochange 
        #Recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y,topleft,tochange)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y,topleft,tochange)
        if y > 0:
            floodfill(matrix,x,y-1,topleft,tochange)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1,topleft,tochange)

#This function returns a list that contains color of elements from surrounding tiles in the block
def checkcolor(matrixcopy,x,y,colorlist,topleft):
	if matrixcopy[x][y] == topleft:
		if x>0:
			colorlist.append(matrixcopy[x-1][y])
		if x < len(matrixcopy[y]) - 1:
			colorlist.append(matrixcopy[x+1][y])
		if y > 0:	
			colorlist.append(matrixcopy[x][y-1])
		if y < len(matrixcopy) - 1:	
			colorlist.append(matrixcopy[x][y+1])
		#Setting the original tile to %(could be any unique character that should NOT BE IN THE ORIGINAL MATRIX)
		matrixcopy[x][y]='%'
		#Recursively check surrounding colors for adjacent tiles
		if (x>0):
			checkcolor(matrixcopy,x-1,y,colorlist,topleft)
		if x < len(matrixcopy[y]) - 1:
			checkcolor(matrixcopy,x+1,y,colorlist,topleft)
		if y > 0:
			checkcolor(matrixcopy,x,y-1,colorlist,topleft)
		if y < len(matrixcopy) - 1:
			checkcolor(matrixcopy,x,y+1,colorlist,topleft)

#This function first removes the original color(topleft) from the list and the dummy color '%'
def most_common(colorlist,topleft):
	colorlist = list(filter(lambda a: a != topleft, colorlist))
	colorlist = list(filter(lambda a: a != '%', colorlist))
	#The Question was a bit ambiguous about the 'lowest rank among colors'. Is this regarding the color palet, alphabetical letters of the color or maybe even karata belt colors :) so I let python do the decision itself. Upon clarification I can edit this to suit the requirement.
	mostcommoncolor = max(set(colorlist), key=colorlist.count)
	print("Most Common Adjacent color is %s"%mostcommoncolor)
	del colorlist
	return mostcommoncolor



if __name__ == "__main__":
	print('Original Matrix:')
	print(np.matrix(matrix))
	print('\n')
	while(len(set.union(*map(set,matrix)))!=1):
		colorlist=[]
		noofmoves=noofmoves+1
		topleft = matrix[0][0]
		matrixcopy = copy.deepcopy(matrix)
		checkcolor(matrixcopy,0,0,colorlist,topleft)
		mostcommoncolor=most_common(colorlist,topleft)
		floodfill(matrix,0,0,topleft,mostcommoncolor)  
		print('Iteration %d:'%noofmoves)
		print(np.matrix(matrix))  
		print('\n')

	print("Number of moves taken = ",noofmoves)
