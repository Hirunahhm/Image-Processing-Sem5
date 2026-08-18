import numpy as np


blank_grid = np.zeros((6, 6))


my_matrix = np.zeros((2, 2))


#initial example matrix with 4 pixel
my_matrix[0, 0] = 90
my_matrix[0, 1] = 80
my_matrix[1, 0] = 70
my_matrix[1, 1] = 60


#function to calculate the average of 4 pixel and return a new matrix with 1 pixel
def scale_up_pixel_cal(matrix, selected_pixel_in_new_matrix):

    matrix_size = matrix.shape[0] * matrix.shape[1]
    #divide the selected pixel in the new matrix by the number of pixels in the original matrix
    average_pixel = selected_pixel_in_new_matrix / matrix_size

    #calculating the pixel value for the new matrix by multiplying the weighted pixel of the orignal matix
    new_pixel_value = 0 
    
