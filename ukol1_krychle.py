def is_valid_coordinate(coord):
    return all(isinstance(val, int) for val in coord)

def is_valid_cube_size(cube_size):
    return cube_size > 0

def is_point_on_wall_floor_ceiling(coord, cube_size):
    return all(0 <= val <= cube_size for val in coord)

def func1(cube_size, coord1, coord2):
    if not (is_valid_cube_size(cube_size) and is_valid_coordinate(coord1) and is_valid_coordinate(coord2)):
        print("Invalid input. Please enter valid numeric values.")
        return

    if not (is_point_on_wall_floor_ceiling(coord1, cube_size) and is_point_on_wall_floor_ceiling(coord2, cube_size)):
        print("Error: The entered point does not lie on any wall/floor/ceiling.")
        return

    n = 0
    if not (cube_size == coord1[2] or cube_size == coord2[2]):
        for i in range(3):
            n += max(coord1[i], coord2[i]) - min(coord1[i], coord2[i])
        return n
    else:
        n1 = (cube_size - coord1[1]) + (cube_size - coord2[1])
        n2 = coord1[1] + coord2[1]
        n3 = (cube_size - coord1[0]) + (cube_size - coord2[0])
        n4 = coord1[0] + coord2[0]
        l = [n1, n2, n3, n4]
        l2 = []
        for i in range(4):
            if i < 2:
                l2 += [max(coord1[0], coord2[0]) - min(coord1[0], coord2[0]) + max(coord1[2], coord2[2]) - min(coord1[2], coord2[2]) + l[i]]
            else:
                l2 += [max(coord1[1], coord2[1]) - min(coord1[1], coord2[1]) + max(coord1[2], coord2[2]) - min(coord1[2], coord2[2]) + l[i]]

        return min(l2)

try:
    cube_size = int(input("Enter cube size: "))
    coord1 = [int(input("Enter coord x for point1: ")), int(input("Enter coord y for point1: ")), int(input("Enter coord z for point1: "))]
    coord2 = [int(input("Enter coord x for point2: ")), int(input("Enter coord y for point2: ")), int(input("Enter coord z for point2: "))]
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
else:
    print(func1(cube_size, coord1, coord2))
