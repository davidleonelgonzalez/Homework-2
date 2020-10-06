# David Gonzalez
# 1630338
def main():
    x_1 = int(input())
    y_1 = int(input())
    num_1 = int(input())

    x_2 = int(input())
    y_2 = int(input())
    num_2 = int(input())

    solution = False

    for x in range(-10, 10):
        for y in range(-10, 10):
            if x_1 * x + y_1 * y == num_1 and x_2 * x + y_2 * y == num_2:
                print(x, y)
                solution = True

    if not solution:
        print('No solution')


main()