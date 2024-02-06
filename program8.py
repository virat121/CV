import cv2
import numpy as np
import math

# Create a black image
image_size = 500
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

# Define cube parameters
cube_size = 100
cube_thickness = 2

# Define cube vertices in 3D space
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]], dtype=np.float32)

# Define cube edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Define colors for each face
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Create a rotation matrix
angle_x, angle_y, angle_z = 0, 0, 0

while True:
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, math.cos(angle_x), -math.sin(angle_x)],
                                  [0, math.sin(angle_x), math.cos(angle_x)]], dtype=np.float32)

    rotation_matrix_y = np.array([[math.cos(angle_y), 0, math.sin(angle_y)],
                                  [0, 1, 0],
                                  [-math.sin(angle_y), 0, math.cos(angle_y)]], dtype=np.float32)

    rotation_matrix_z = np.array([[math.cos(angle_z), -math.sin(angle_z), 0],
                                  [math.sin(angle_z), math.cos(angle_z), 0],
                                  [0, 0, 1]], dtype=np.float32)

    # Rotate the cube vertices in 3D space
    rotated_vertices = np.dot(vertices, rotation_matrix_x)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_y)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_z)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([image_size // 2, image_size // 2])).astype(int)

    # Create a black image
    image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

    # Draw cube faces
    for i, face in enumerate([(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
                              (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)]):
        pts = projected_vertices[face, :]
        cv2.fillPoly(image, [pts], color=colors[i])

    # Draw cube edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(image, pt1, pt2, (255, 255, 255), cube_thickness)

    # Display the frame
    cv2.imshow("Rotating 3D Cube", image)

    # Wait for a moment and update the angles
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

    angle_x += 0.02
    angle_y += 0.02
    angle_z += 0.02

# Release the window
cv2.destroyAllWindows()
