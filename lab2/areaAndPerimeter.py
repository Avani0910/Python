# Function to calculate area and perimeter of a rectangle
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area, perimeter = rectangle_properties(length, width)

print(f"\nArea of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
