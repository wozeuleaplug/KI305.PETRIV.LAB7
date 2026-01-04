def generate_list(n: int, m: int, fill: str) -> list[str]:
    """
    Генерує список довжини n.
    В середині (відносно центру) вікно радіуса m заповнюється пробілами,
    решта — символом fill. Працює симетрично для парного і непарного n.
    """
    center = (n - 1) / 2
    return [' ' if abs(i - center) <= m else fill for i in range(n)]


def generate_matrix(n: int, fill: str) -> list[list[str]]:
    """
    Генерує квадратну матрицю n×n (список списків),
    де для кожного рядка m росте до середини, а потім зменшується.
    """
    matrix = []
    for row in range(n):
        # m росте до середини, потім зменшується
        m_row = row if row <= (n - 1) // 2 else (n - 1 - row)
        matrix.append(generate_list(n, m_row, fill))
    return matrix


def print_matrix(matrix: list[list[str]]) -> None:
    """Друкує матрицю у вигляді символів."""
    for row in matrix:
        print(''.join(row))


def read_size(max_n: int = 50) -> int:
    """
    Зчитує розмір матриці n.
    Перевіряє, що введено ціле число в межах 1..max_n.
    """
    raw = input(f"Введіть розмір матриці n (ціле число 1..{max_n}): ").strip()

    try:
        n = int(raw)
    except ValueError:
        print("Помилка: розмір матриці має бути цілим числом.")
        raise SystemExit(1)

    if not (1 <= n <= max_n):
        print(f"Помилка: n має бути в межах 1..{max_n}.")
        raise SystemExit(1)

    return n


def read_fill_char() -> str:
    """
    Зчитує символ-заповнювач.
    Перевіряє, що введено рівно один символ і це не пробіл.
    """
    raw = input("Введіть символ-заповнювач (один символ, наприклад #): ")
    fill = raw.strip()

    if len(fill) == 0:
        print("Помилка: символ-заповнювач не може бути порожнім.")
        raise SystemExit(1)

    if len(fill) != 1:
        print("Помилка: введіть рівно один символ.")
        raise SystemExit(1)

    if fill == ' ':
        print("Помилка: символ-заповнювач не може бути пробілом.")
        raise SystemExit(1)

    return fill


def main() -> None:
    # Максимально дозволений розмір матриці
    MAX_N = 50

    n = read_size(MAX_N)
    fill = read_fill_char()

    mat = generate_matrix(n, fill)
    print_matrix(mat)


if __name__ == "__main__":
    main()