import cv2
import numpy as np

# Create a blank black image
image_size = (500, 500, 3)  # Width, height, and channels (RGB)
image = np.zeros(image_size, dtype=np.uint8)  # Initialize with black color

# Draw a square
square_pts = np.array([[100, 100], [100, 300], [300, 300], [300, 100]], np.int32)
square_pts = square_pts.reshape((-1, 1, 2))
cv2.fillPoly(image, [square_pts], color=(0, 255, 0))  # Green color

# Draw a circle
center = (400, 100)
radius = 50
cv2.circle(image, center, radius, color=(255, 0, 0), thickness=-1)  # Blue color, -1 for filled circle

# Display the image
cv2.imshow('Colorful 2D Objects Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
