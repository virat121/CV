import cv2
import numpy as np
import math

# Create a window
cv2.namedWindow("Rotating 3D Cube", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rotating 3D Cube", 600, 600)

# Set initial cube parameters
cube_size = 75
cube_color = (255, 0, 0)
edge_color = (255, 255, 255)
background_color = (0, 0, 0)
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

# Create a rotation matrix
angle = 0

paused = False  # Flag to check if rotation is paused

while True:
    if not paused:
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                    [math.sin(angle), math.cos(angle), 0],
                                    [0, 1, 1]], dtype=np.float32)

        # Rotate the cube vertices in 3D space
        rotated_vertices = np.dot(vertices, rotation_matrix)

        # Project the 3D points to 2D
        projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

        # Create a black image
        frame = np.ones((600, 600, 3), dtype=np.uint8) * background_color

        # Draw cube edges
        for edge in edges:
            pt1 = tuple(projected_vertices[edge[0]])
            pt2 = tuple(projected_vertices[edge[1]])
            cv2.line(frame, pt1, pt2, edge_color, cube_thickness)

        # Display the frame
        cv2.imshow("Rotating 3D Cube", frame.astype(np.uint8))

        # Wait for a moment and update the angle
        key = cv2.waitKey(30)

        # Check if 's' key is pressed to toggle rotation pause
        if key == ord('s'):
            paused = not paused

        # Check if 'e' key is pressed to change the edge color
        elif key == ord('e'):
            edge_color = np.random.randint(0, 256, size=3).tolist()

        # Check if 'b' key is pressed to change the background color
        elif key == ord('b'):
            background_color = np.random.randint(0, 256, size=3).tolist()

        # Check if 'q' key is pressed to exit the program
        elif key == ord('q'):
            break

        angle += 0.03  # Adjusted rotation speed

# Release the window
cv2.destroyAllWindows()
