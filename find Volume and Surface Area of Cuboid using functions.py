# Python Program to find Volume and Surface Area of a Cuboid using Functions

def Vo_Sa_Cuboid(length, width, height):
    # Calculate the Surface Area
    SA = 2 * (length * width + length * height + width * height)

    # Calculate the Volume
    Volume = length * width * height

    # Calculate the Lateral Surface Area
    LSA = 2 * height * (length + width)

    print("\n The Surface Area of a Cuboid = %.2f " %SA)
    print(" The Volume of a Cuboid = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cuboid = %.2f " %LSA)

Vo_Sa_Cuboid(9, 4, 6)
