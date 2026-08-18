import numpy as np


blank_grid = np.zeros((6, 6))


my_matrix = np.zeros((2, 2))


#initial example matrix with 4 pixel
my_matrix[0, 0] = 90
my_matrix[0, 1] = 80
my_matrix[1, 0] = 70
my_matrix[1, 1] = 60


#function to calculate the average of 4 pixel and return a new matrix with 1 pixel
def scale_up_pixel_cal(matrix, selected_pixel_in_new_matrix, new_shape):

    scale_row = new_shape[0] / matrix.shape[0]
    scale_col = new_shape[1] / matrix.shape[1]
    #divide the selected pixel in the new matrix by the number of pixels in the original matrix
    new_row, new_col = selected_pixel_in_new_matrix  #this is an array[x, y]

    #calculating the pixel value for the new matrix by multiplying the weighted pixel of the orignal matix
    #new_pixel_value = 0 

    x = new_row / scale_row
    y = new_col / scale_col

    

    top_left_row = int(x)
    top_left_col = int(y)

    dx = x - top_left_row
    dy = y - top_left_col

    bottom_right_row = min(top_left_row + 1, matrix.shape[0] - 1)
    bottom_right_col = min(top_left_col + 1, matrix.shape[1] - 1)

    #new_pixel_value = 0

    top_left_pixel = matrix[top_left_row, top_left_col]
    top_right_pixel = matrix[top_left_row, bottom_right_col]
    bottom_left_pixel = matrix[bottom_right_row, top_left_col]
    bottom_right_pixel = matrix[bottom_right_row, bottom_right_col]

    
        #for j in range(1,matrix.shape[1]+1):

            #if i <= x and j <= y:
                #new_pixel_value += matrix[i-1, j-1] * (i -dx) * (j - dy)

            #elif i <= x and j > y:
                #new_pixel_value += matrix[i-1, j-1] * (i - dx) * (dy)

           # elif i > x and j <= y:
                #new_pixel_value += matrix[i-1, j-1] * (dx) * (j - dy)

            #elif i > x and j > y:
               # new_pixel_value += matrix[i-1, j-1] * (dx) * (dy)  


    new_pixel_value = (
        top_left_pixel * (1 - dx) * (1 - dy) +
        top_right_pixel * (1 - dx) * dy +
        bottom_left_pixel * dx * (1 - dy) +
        bottom_right_pixel * dx * dy
    )

    return new_pixel_value




for i in range(blank_grid.shape[0]):
    for j in range(blank_grid.shape[1]):
        blank_grid[i, j] = scale_up_pixel_cal(my_matrix, [i, j], blank_grid.shape)



print(blank_grid)


