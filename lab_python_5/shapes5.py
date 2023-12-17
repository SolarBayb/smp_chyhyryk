import math

class Star3D:
    ANSI_COLOR_CODES = {
        'red': '\033[31m',
        'green': '\033[32m',
        'blue': '\033[34m',
        'yellow': '\033[33m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'black': '\033[30m',
        'reset': '\033[0m'  # Resets the color to default
    }

    def __init__(self, spikes, outer_radius, inner_radius, depth, symbol):
        self.spikes = spikes
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.depth = depth
        self.symbol = symbol
        self.color_code = 7  # Default to white
        self.center_x = self.outer_radius + 1
        self.center_y = self.outer_radius + 1
        self.rotation_angle = 0  # Initialize rotation_angle before calculate_vertices
        self.vertices = self.calculate_vertices()
        self.is_3d_mode = False  # Start in 2D mode

    color_table = {
        1: 'red',
        2: 'green',
        3: 'blue',
        4: 'yellow',
        5: 'purple',
        6: 'cyan',
        7: 'white',
        8: 'black'
    }

    def __str__(self):
        # Construct a string representation of the star's current state
        star_info = [
            f"Spikes: {self.spikes}",
            f"Outer Radius: {self.outer_radius}",
            f"Inner Radius: {self.inner_radius}",
            f"Depth: {self.depth}",
            f"Symbol: '{self.symbol}'",
            f"Color: {self.color_table[self.color_code]}",
            f"Center: ({self.center_x}, {self.center_y})",
            f"Rotation Angle: {self.rotation_angle}",
            f"3D Mode: {'Enabled' if self.is_3d_mode else 'Disabled'}"
        ]
        return "Star3D(" + ', '.join(star_info) + ")"

    def calculate_vertices(self):
        """Calculate the vertices of the star in 2D."""
        vertices = []
        start_angle = math.radians(self.rotation_angle)
        for i in range(self.spikes * 2):
            angle = start_angle + i * (math.pi / self.spikes)
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            vertices.append((x, y, 0))  # 2D representation
        return vertices

    def set_size(self, spikes, outer_radius, inner_radius, depth):
        self.spikes = spikes
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.depth = depth
        self.vertices = self.calculate_vertices()

    def choose_color(self):
        print("Available colors:")
        for number, color in self.color_table.items():
            print(f"{number}: {color}")
        color_code = int(input("Enter the color code: "))
        if color_code in self.color_table:
            self.color_code = color_code
            print(f"Color changed to {self.color_table[color_code]}")
        else:
            print("Invalid color code.")

    def set_symbol(self, symbol):
        self.symbol = symbol


    def scale(self, scale_factor):
        """Scales the star's size by a given factor."""
        self.outer_radius *= scale_factor
        self.inner_radius *= scale_factor
        self.vertices = self.calculate_vertices()

    def toggle_projection(self):
        """Toggle between 3D and 2D projections."""
        self.is_3d_mode = not self.is_3d_mode
        print("Toggled to", "3D" if self.is_3d_mode else "2D", "mode.")

    def draw_star(self):
        """Draws the star based on its vertices."""
        # Initialize the size of the grid
        size = int(self.outer_radius * 2 + 2)
        grid = [[' ' for _ in range(size)] for _ in range(size)]

        # Choose vertices based on the current mode
        vertices = self.vertices if self.is_3d_mode else self.project_to_2d()

        # Draw lines between the vertices
        for i in range(len(vertices)):
            start_vertex = vertices[i]
            end_vertex = vertices[(i + 1) % len(vertices)]
            self.draw_line(grid, start_vertex[0], start_vertex[1], end_vertex[0], end_vertex[1])

        # Print the star grid
        for row in grid:
            print(''.join(row))

        # Convert 3D vertices to 2D if necessary
        vertices_2d = self.project_to_2d()

        # Draw lines between the vertices
        for i in range(len(vertices_2d)):
            start_vertex = vertices_2d[i]
            end_vertex = vertices_2d[(i + 1) % len(vertices_2d)]
            self.draw_line(grid, *start_vertex, *end_vertex)

        # Print the star grid
        for row in grid:
            print(''.join(row))

    def draw_line(self, grid, x0, y0, x1, y1):
        """Draws a line on the grid from (x0, y0) to (x1, y1) using Bresenham's algorithm."""
        # Convert coordinates to integers
        x0, y0, x1, y1 = map(int, [x0, y0, x1, y1])

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        # Get the ANSI color code
        color_code = self.ANSI_COLOR_CODES[self.color_table[self.color_code]]

        while True:
            if 0 <= x0 < len(grid) and 0 <= y0 < len(grid[0]):
                grid[y0][x0] = color_code + self.symbol + self.ANSI_COLOR_CODES['reset']

            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def rotate_3d(self, x_angle, y_angle, z_angle):
        """Rotates the star in 3D space."""
        # Convert angles to radians
        x_angle = math.radians(x_angle)
        y_angle = math.radians(y_angle)
        z_angle = math.radians(z_angle)

        rotated_vertices = []
        for x, y, z in self.vertices:
            # Rotation around the X-axis
            y_rotated = y * math.cos(x_angle) - z * math.sin(x_angle)
            z_rotated = y * math.sin(x_angle) + z * math.cos(x_angle)

            # Rotation around the Y-axis
            x_rotated = x * math.cos(y_angle) + z_rotated * math.sin(y_angle)
            z_rotated = -x * math.sin(y_angle) + z_rotated * math.cos(y_angle)

            # Rotation around the Z-axis
            x_rotated = x_rotated * math.cos(z_angle) - y_rotated * math.sin(z_angle)
            y_rotated = x_rotated * math.sin(z_angle) + y_rotated * math.cos(z_angle)

            rotated_vertices.append((x_rotated, y_rotated, z_rotated))

        self.vertices = rotated_vertices

    def project_to_2d(self):
        """Projects the 3D star to 2D."""
        return [(x, y) for x, y, z in self.vertices]

    def calculate_vertices(self):
        """Calculate the vertices of the star."""
        vertices = []
        start_angle = math.radians(self.rotation_angle)  # Convert the rotation angle to radians
        for i in range(self.spikes * 2):
            angle = start_angle + i * (math.pi / self.spikes)
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = self.center_x + radius * math.cos(angle)
            y = self.center_y + radius * math.sin(angle)
            vertices.append((x, y, 0))  # Assuming a z-coordinate of 0 for 2D representation
        return vertices

    def prompt_for_rotation(self):
        """Prompts the user to enter rotation angles and applies the rotation."""
        while True:
            try:
                x_angle = float(input("Enter rotation angle in degrees for X-axis: "))
                y_angle = float(input("Enter rotation angle in degrees for Y-axis: "))
                z_angle = float(input("Enter rotation angle in degrees for Z-axis: "))

                self.rotate_3d(x_angle, y_angle, z_angle)
                break  # Correctly placed inside the loop
            except ValueError:
                print("Invalid input. Please enter valid numbers for X, Y, and Z angles.")

    def move_left(self, step=1):
        """Move the star to the left by a specified number of steps."""
        self.center_x = max(1, self.center_x - step)
        self.vertices = self.calculate_vertices()

    def move_right(self, step=1):
        """Move the star to the right by a specified number of steps."""
        self.center_x += step
        self.vertices = self.calculate_vertices()

    def move_up(self, step=1):
        """Move the star up by a specified number of steps."""
        self.center_y = max(1, self.center_y - step)
        self.vertices = self.calculate_vertices()

    def move_down(self, step=1):
        """Move the star down by a specified number of steps."""
        self.center_y += step
        self.vertices = self.calculate_vertices()

    def center_star(self):
        """Center the star on the grid."""
        self.center_x = self.outer_radius + 1
        self.center_y = self.outer_radius + 1
        self.vertices = self.calculate_vertices()

