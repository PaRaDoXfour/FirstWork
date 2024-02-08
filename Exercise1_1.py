a = float(input("Введіть а: "))

while a < 1:
    a = float(input("Введіть а: "))

b = float(input("Введіть b: "))

while b < 1:

    b = float(input("Введіть ще раз b: "))

    if a > b:
        result = a * b + 1
    elif a == b:
        result = -10
    else:
        result = (a - 5) / b

print("Результат обчислення виразу: ", result)
