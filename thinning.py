from skimage import io
import matplotlib.pyplot as plt
from zhang_suen_function import zhang_suen

# -------------------------------------------
# Load the image
image_file = "hwimg.png" 
img = io.imread(image_file, as_gray=True)

# -------------------------------------------
# Plot the untouched image
plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.show()

# -------------------------------------------
# Apply a filter to create binary version of the image
from skimage.filters import threshold_otsu
Otsu_Threshold = threshold_otsu(img)   
binary_img = img < Otsu_Threshold
binary_img = binary_img * 1

'''NOTE: UNCOMMENT THE FOLLOWING LINE IF binary_img's SHAPE IS (218, 150, 4)
INSTEAD OF (218, 150). I NOTICED THAT THIS OCCURS WHEN USING PYTHON 3.6. TO MY
KNOWLEDGE, IT LOADS CORRECTLY USING PYTHON 3.5 '''
binary_img = binary_img[:, :, 1]

# -------------------------------------------
# Plot the binary image
plt.figure()
plt.imshow(binary_img, cmap='gray')
plt.title('Binary Image')
plt.show()

# -------------------------------------------
# Call the zhang-suen thinning function, 
# apply it to the binary image, 
# and plot the result
plt.figure()
thinned_img = zhang_suen(binary_img)
plt.imshow(thinned_img, cmap='gray')
plt.title('Thinned Image')
plt.show()



