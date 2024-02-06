import cv2
import numpy as np

# Read the input color image
image = cv2.imread("./baby_img.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Define a smaller kernel for milder morphological operations
    kernel_size = 3
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Erosion
    eroded_image = cv2.erode(image, kernel, iterations=5)

    # Dilation
    dilated_image = cv2.dilate(image, kernel, iterations=5)

    # Resize images for better visibility
    scale_factor = 0.1  # Adjust the scale factor as needed
    resized_original = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    resized_eroded = cv2.resize(eroded_image, None, fx=scale_factor, fy=scale_factor)
    resized_dilated = cv2.resize(dilated_image, None, fx=scale_factor, fy=scale_factor)

    # Display the original, eroded, and dilated images
    cv2.imshow("Original Image", resized_original)
    cv2.imshow("Eroded Image", resized_eroded)
    cv2.imshow("Dilated Image", resized_dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
