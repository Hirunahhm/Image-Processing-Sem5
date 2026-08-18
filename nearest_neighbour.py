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

    #find the scale factor for row and column
    scale_row = new_shape[0] / matrix.shape[0]
    scale_col = new_shape[1] / matrix.shape[1]
    
    new_row, new_col = selected_pixel_in_new_matrix  #this is an array[x, y]

    #calculating the pixel value for the new matrix by multiplying the weighted pixel of the orignal matix
    #new_pixel_value = 0 

    x = new_row / scale_row
    y = new_col / scale_col

    nearest_row = round(x)
    nearest_col = round(y)

    # Ensure we don't go out of bounds on the bottom/right edges
    nearest_row = min(nearest_row, matrix.shape[0] - 1)
    nearest_col = min(nearest_col, matrix.shape[1] - 1)

    return matrix[nearest_row, nearest_col]




for i in range(blank_grid.shape[0]):
    for j in range(blank_grid.shape[1]):
        blank_grid[i, j] = scale_up_pixel_cal(my_matrix, [i, j], blank_grid.shape)



print(blank_grid)


