"""Compute and print the volume of a right circular cone."""
    
    # Import the standard math module so that
    # math.pi can be used in this program.
import math
    
    
def main():
        # Call the cone_volume function to compute
        # the volume of an example cone.
#
    
        # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))
    
        # Call the cone_volume function to compute the volume
        # for the radius and height that came from the user.
    vol = cone_volume(radius, height)
    
        # Print the radius, height, and
        # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")
    
def cone_volume(radius, height):
    #"""Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume
    
    
    # Start this program by
    # calling the main function.
main()