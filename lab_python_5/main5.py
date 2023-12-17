from shapes5 import Star3D
import sys
import io
from Scripts.all_python_labs.shared_lib.runnable import Runnable

def run(self):
    """
    Run the main application loop.

    Returns:
    - None
    """
    # Run the main application event loop
    self.root.mainloop()

def main():
    # Create a star object with default parameters
    star = Star3D(spikes=5, outer_radius=1, inner_radius=1, depth=1, symbol='*')

    def save_star_to_file(star, filename="star_output.txt"):
        # Save the original stdout
        original_stdout = sys.stdout

        # Create a string buffer to capture the output
        buffer = io.StringIO()

        # Redirect stdout to the buffer
        sys.stdout = buffer

        # Draw the star in its current mode (2D or 3D)
        star.draw_star()

        # Reset stdout to its original value
        sys.stdout = original_stdout

        # Get the content from the buffer
        star_output = buffer.getvalue()

        # Write the captured output to a file
        with open(filename, "w") as f:
            f.write(star_output)

        # Close the buffer
        buffer.close()


    while True:
        print("\nMain Menu:")
        print("1. Set Star Size")
        print("2. Set Star Color")
        print("3. Set Star Symbol")
        print("4. Draw Star")
        print("5. Move Star")
        print("6. Scale Star")
        print("7. Rotate Star")
        print("8. Toggle 3D/2D View")
        print("9. Save Star to File")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            spikes = int(input("Enter the number of spikes: "))
            outer_radius = int(input("Enter the outer radius: "))
            inner_radius = int(input("Enter the inner radius: "))
            depth = int(input("Enter the depth: "))
            star.set_size(spikes, outer_radius, inner_radius, depth)
        elif choice == "2":
            star.choose_color()
        elif choice == "3":
            symbol = input("Enter the symbol to use for drawing the star: ")
            star.set_symbol(symbol)
        elif choice == "4":
            star.draw_star()
        elif choice == "5":
            direction = input("Enter direction (left, right, up, down): ")
            step = int(input("Enter steps to move: "))
            if direction == "left":
                star.move_left(step)
            elif direction == "right":
                star.move_right(step)
            elif direction == "up":
                star.move_up(step)
            elif direction == "down":
                star.move_down(step)
            else:
                print("Invalid direction.")

        elif choice == "6":
            star.center_star()


        elif choice == "7":

            x_angle = float(input("Enter rotation angle in degrees for X-axis: "))
            y_angle = float(input("Enter rotation angle in degrees for Y-axis: "))
            z_angle = float(input("Enter rotation angle in degrees for Z-axis: "))
            star.rotate_3d(x_angle, y_angle, z_angle)

        elif choice == "8":

            star.toggle_projection()  # Assuming you have a method to toggle between 3D and 2D


        elif choice == "9":
            save_star_to_file(star)  # Save the current state of the star
            # Save 2D projection
            star.toggle_projection()  # Ensure it's in 2D mode
            save_star_to_file(star, "star_2d_output.txt")

            # Save 3D projection
            star.toggle_projection()  # Switch to 3D mode
            save_star_to_file(star, "star_3d_output.txt")
            print(f"Star state saved to file.")

        elif choice == "10":

            print("Goodbye!")

            break
        else:

            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
