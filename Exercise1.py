def calculate_x(a, b):
    if a > b:
        result = a * b + 1
    elif a == b:
        result = -10
    else:
        result = (a - 5) / b
    return result


def main():
    try:
        a = float(input("Введіть значення a (додатнє число): "))
        b = float(input("Введіть значення b (додатнє число): "))

        if a <= 0 or b <= 0:
            print("Помилка: a та b повинні бути додатніми числами.")
        else:
            result = calculate_x(a, b)
            print(f"Значення X: {result}")
    except ValueError:
        print("Помилка: Введено некоректне значення. Введіть додатнє число.")


if __name__ == "__main__":
    main()
