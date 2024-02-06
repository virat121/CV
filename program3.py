import cv2
import numpy as np
import math

# Callback function for trackbar changes
def on_size_change(value):
    global circle_radius, cube_size
    circle_radius = value
    cube_size = value

# Create a black canvas with a white circle (2D Image)
img_2d = np.zeros((300, 300, 3), dtype=np.uint8)

# Initial parameters for 2D Image
circle_center = (150, 150)
circle_color = (255, 255, 255)

# Initial parameters for 3D Image
cube_size = 100
cube_color = (0, 255, 0)
cube_thickness = 2

# Define cube edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Create a rotation matrix
angle = 0

# Create a resizable window
cv2.namedWindow("Resizable 2D and 3D Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resizable 2D and 3D Images", 400, 400)

# Create a trackbar for resizing
cv2.createTrackbar("Size", "Resizable 2D and 3D Images", cube_size, 200, on_size_change)

while True:
    # Resize 2D Image (Circle)
    img_2d = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.circle(img_2d, circle_center, circle_radius, circle_color, -1)
    cv2.imshow("Resizable 2D Image", img_2d)

    # Resize 3D Image (Rotate Cube)
    vertices = np.array([[-1, -1, -1],
                         [1, -1, -1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, 1],
                         [-1, 1, 1]], dtype=np.float32)

    # Scale the cube vertices
    scaled_vertices = vertices * (cube_size / 100)

    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)

    # Rotate the cube vertices in 3D space
    rotated_vertices = np.dot(scaled_vertices, rotation_matrix)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([200, 200])).astype(int)

    # Create a black image
    frame = np.zeros((400, 400, 3), dtype=np.uint8)

    # Draw cube edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Resizable 3D Image", frame)

    # Update angle for rotating the 3D cube
    angle += 0.02

    key = cv2.waitKey(30)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
