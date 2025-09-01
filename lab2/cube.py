# Write a python code for calculate the area and volume of the Cube. 5

# Function to calculate area and volume of a cube
def cube_properties(side_length):
    surface_area = 6 * (side_length ** 2)
    volume = side_length ** 3
    return surface_area, volume

# Example usage
side = float(input("Enter the side length of the cube: "))
area, volume = cube_properties(side)

print(f"\nSurface Area of the cube: {area}")
print(f"Volume of the cube: {volume}")
