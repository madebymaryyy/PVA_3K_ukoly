import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_closest_planes(planes):
    min_distance = float('inf')
    closest_pairs = []
    for i in range(len(planes)):
        for j in range(i+1, len(planes)):
            dist = calculate_distance(planes[i][0], planes[j][0])
            if dist < min_distance:
                min_distance = dist
                closest_pairs = [(planes[i][1], planes[j][1])]
            elif dist == min_distance:
                closest_pairs.append((planes[i][1], planes[j][1]))
    return min_distance, closest_pairs

planes = []
while True:
    try:
        line = input()
        if not line:
            break
        coords, name = line.split(':')
        x, y = map(float, coords.split(','))
        planes.append(((x, y), name))
    except Exception:
        print("Chyba: nesprávný formát vstupu")
        break

if len(planes) < 2:
    print("Chyba: méně než dvě letadla na vstupu")
else:
    min_distance, pairs = find_closest_planes(planes)
    print("Vzdálenost nejbližších letadel: {:.6f}".format(min_distance))
    print("Nalezených dvojic: {}".format(len(pairs)))
    for pair in pairs:
        print(" - ".join(pair))
