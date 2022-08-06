from random import randint as rnum

def spawn():
    if rnum(1, 50) == 1:
        return True
    else:
        return False


def render(matrix: list, density: int):
    drop = [".", "o", "O", " "]
    for i in range(len(matrix)):
        if matrix[i] in drop[0:-1]:
            matrix[i] = drop[drop.index(matrix[i]) + 1]
        elif spawn():
            matrix[i] = "."
    return matrix

def main(x_max: int = 75, y_max: int = 27, density: int = 50):
    buffer = 5
    matrix = [" "] * x_max
    height = y_max + buffer

    for i in range(height):
        matrix = render(matrix, density)
        if i >= buffer:
            print(''.join(matrix))


if __name__ == "__main__":
    x_max = int(input("Please enter width of render   >> "))
    y_max = int(input("Please enter height of render  >> "))
    dense = int(input("Please enter spawn rate (1inX) >> "))
    main(x_max=x_max, y_max=y_max, density=dense)
