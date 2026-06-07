"""Calculate the surface area of a cuboid."""


def surface_area_cuboid(length, breadth, height):
    return 2 * (length * breadth + breadth * height + length * height)


try:
    length = float(input("Length: "))
    breadth = float(input("Breadth: "))
    height = float(input("Height: "))

    if length < 0 or breadth < 0 or height < 0:
        print("Length, breadth, and height cannot be negative.")
    else:
        area = surface_area_cuboid(length, breadth, height)
        print(f"Surface area = {area:.2f}")
except ValueError:
    print("Please enter valid numbers.")
