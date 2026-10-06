import random


def input_size():
    while True:
        try:
            m = int(input("Введите количество строк: "))
            n = int(input("Введите количество столбцов: "))

            if m > 0 and n > 0:
                return m, n

            print("Размеры должны быть больше 0.")

        except ValueError:
            print("Введите целые числа.")


def generate_matrix(m, n):
    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(round(random.uniform(-10, 10), 2))
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


def sort_even_rows(matrix):
    for i in range(1, len(matrix), 2):
        for j in range(len(matrix[i]) - 1):
            for k in range(len(matrix[i]) - 1 - j):
                if matrix[i][k] > matrix[i][k + 1]:
                    matrix[i][k], matrix[i][k + 1] = matrix[i][k + 1], matrix[i][k]


def main():
    m, n = input_size()

    matrix = generate_matrix(m, n)

    print("Исходная матрица:")
    print_matrix(matrix)

    sort_even_rows(matrix)

    print("Результат:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()