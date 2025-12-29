# array.py
import sys

def generate_array(n, fill_char):
    result = []
    center = n // 2
    
    for i in range(n):
        row = []
        for j in range(n):
            # Distance from center
            dist_i = abs(i - center)
            dist_j = abs(j - center)
            
            # Condition for empty diamond inside
            if dist_i + dist_j <= center:
                # Inside diamond - empty
                row.append(" ")
            else:
                # Outside diamond - check if in corners
                if (i < center and j < center) or \
                   (i < center and j > center) or \
                   (i > center and j < center) or \
                   (i > center and j > center):
                    # In one of the four corners
                    row.append(fill_char)
                else:
                    # On the edges but not in corners
                    row.append(" ")
        result.append(row)
    
    return result

def main():
    try:
        n = int(input("Enter matrix size: "))
        fill_char = input("Enter fill character: ")

        if fill_char == "":
            print("Error: fill character cannot be empty.")
            sys.exit(1)
        elif len(fill_char) > 1:
            print("Error: only one character allowed.")
            sys.exit(1)

        array = generate_array(n, fill_char)

        print(f"\nGenerated array (size: {n}, fill: '{fill_char}'):")
        for row in array:
            print(' '.join(row))

    except ValueError:
        print("Error: size must be an integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()