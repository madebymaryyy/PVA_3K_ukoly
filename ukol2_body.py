def are_collinear(A, B, C):
    return (B[1] - A[1]) * (C[0] - B[0]) == (C[1] - B[1]) * (B[0] - A[0])

def midpoint(A, B, C):
    if are_collinear(A, B, C):
        if A[0] <= B[0] <= C[0] or C[0] <= B[0] <= A[0]:
            return B
        elif B[0] <= A[0] <= C[0] or C[0] <= A[0] <= B[0]:
            return A
        else:
            return C
    else:
        return None

def parse_input(input_str):
    try:
        coords = [float(coord) for coord in input_str.split()]
        if len(coords) != 2:
            raise ValueError("Invalid input format")
        return tuple(coords)
    except ValueError:
        raise ValueError("Invalid input format")

def main():
    try:
        input_A = input("Bod A:\n")
        A = parse_input(input_A)
        input_B = input("Bod B:\n")
        B = parse_input(input_B)
        input_C = input("Bod C:\n")
        C = parse_input(input_C)

        if A == B == C:
            print("Dva nebo všechny tři zadané body splývají.")
        elif A == B or A == C or B == C:
            print("Některé body splývají.")
        elif are_collinear(A, B, C):
            print("Body leží na jedné přímce.")
            mid = midpoint(A, B, C)
            if mid:
                if mid == A:
                    print(f"Prostřední je bod A.")
                elif mid == B:
                    print(f"Prostřední je bod B.")
                else:
                    print(f"Prostřední je bod C.")
        else:
            print("Body neleží na jedné přímce.")
    except ValueError as e:
        print("Chyba:", e)

if __name__ == "__main__":
    main()
