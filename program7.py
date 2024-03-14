import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Initialize triangle vertices
triangle_vertices = np.array([[250, 50], [50, 450], [450, 450]], dtype=np.int32)

# Draw the triangle
cv2.polylines(image, [triangle_vertices], isClosed=True, color=(0, 255, 0), thickness=2)

# Calculate the centroid of the triangle
centroid = np.mean(triangle_vertices, axis=0, dtype=np.int32)

# Display the centroid
cv2.circle(image, tuple(centroid), radius=5, color=(0, 0, 255), thickness=-1)

# Display the image
cv2.imshow("Triangle with Centroid", image)
cv2.waitKey(0)

# Create a function to change the color on mouse click
def change_color(event, x, y, flags, param):
    global image

    if event == cv2.EVENT_LBUTTONDOWN:
        # Change the color of the triangle
        new_color = np.random.randint(0, 256, size=3).tolist()
        cv2.polylines(image, [triangle_vertices], isClosed=True, color=new_color, thickness=2)
        cv2.circle(image, tuple(centroid), radius=5, color=(0, 0, 255), thickness=-1)
        cv2.imshow("Triangle with Centroid", image)

# Set the callback function for mouse events
cv2.setMouseCallback("Triangle with Centroid", change_color)

# Wait for a key press and close the window on 'q' press
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the window
cv2.destroyAllWindows()