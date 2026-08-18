import numpy as np
from PIL import Image

# Load the image and convert it to a NumPy matrix
image_name = 'Image_processing_sample.jpg'

original_img = Image.open(image_name).convert('RGB')
original_matrix = np.array(original_img)


# Nearest Neighbor Algorithm
def nearest_neighbor_pixel(matrix, new_row, new_col, scale_row, scale_col):
    x = new_row / scale_row
    y = new_col / scale_col
    nearest_row = min(round(x), matrix.shape[0] - 1)
    nearest_col = min(round(y), matrix.shape[1] - 1)
    return matrix[nearest_row, nearest_col]

# Bilinear Algorithm
def bilinear_pixel(matrix, new_row, new_col, scale_row, scale_col):

    x = new_row / scale_row
    y = new_col / scale_col

    top_left_row = int(x)
    top_left_col = int(y)

    dx = x - top_left_row
    dy = y - top_left_col

    bottom_right_row = min(top_left_row + 1, matrix.shape[0] - 1)
    bottom_right_col = min(top_left_col + 1, matrix.shape[1] - 1)
    
    top_left_pixel = matrix[top_left_row, top_left_col]
    top_right_pixel = matrix[top_left_row, bottom_right_col]
    bottom_left_pixel = matrix[bottom_right_row, top_left_col]
    bottom_right_pixel = matrix[bottom_right_row, bottom_right_col]
    
    new_pixel_value = (
        top_left_pixel * (1 - dx) * (1 - dy) +
        top_right_pixel * (1 - dx) * dy +
        bottom_left_pixel * dx * (1 - dy) +
        bottom_right_pixel * dx * dy
    )
    return new_pixel_value

# main function to loop through the grid
def resize_image(original_matrix, scale_factor, method):
    old_height, old_width, channels = original_matrix.shape
    new_height = int(old_height * scale_factor)
    new_width = int(old_width * scale_factor)
    new_matrix = np.zeros((new_height, new_width, channels), dtype=np.uint8)
    scale_row = new_height / old_height
    scale_col = new_width / old_width
    
    for i in range(new_height):
        for j in range(new_width):
            if method == 'nearest':
                new_matrix[i, j] = nearest_neighbor_pixel(original_matrix, i, j, scale_row, scale_col)
            elif method == 'bilinear':
                new_matrix[i, j] = bilinear_pixel(original_matrix, i, j, scale_row, scale_col)
                
    return new_matrix

#Process the image
SCALE = 2.0  
print(f"Scaling image by {SCALE}x")

print("Running Nearest Neighbor")
nn_matrix = resize_image(original_matrix, scale_factor=SCALE, method='nearest')

print("nearest neghbour matrix: ", nn_matrix)
print("Running Bilinear Interpolation")
bl_matrix = resize_image(original_matrix, scale_factor=SCALE, method='bilinear')

print("bilinear matrix: ", bl_matrix)

# results to the folder
print("Saving images to the folder")
Image.fromarray(nn_matrix).save("nearest_neighbor_output.jpg")
Image.fromarray(bl_matrix).save("bilinear_output.jpg")

print("Done! Saved the new images.")