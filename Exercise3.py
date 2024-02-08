N = int(input("Введіть число від 1 до 10: "))

if N == 1:
    for i in range(5, 0, -1):
        print(' '.join(map(str, range(i, 6))))

elif N == 2:
    for i in range(1, 6):
        print(' '.join(map(str, range(1, 7 - i))))

elif N == 3:
    for i in range(1, 6):
        print(' '.join(map(str, range(1, i + 1))))

elif N == 4:
    for i in range(5, 0, -1):
        print(' '.join(map(str, range(5, 5 - i, -1))))

elif N == 5:
    for i in range(5, 0, -1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print()

elif N == 5:
    for i in range(5, 0, -1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print()

elif N == 6:
    for i in range(1, 6):
        print(' '.join(map(str, range(i, 0, -1))))

elif N == 7:
    for i in range(1, 6):
        print(' '.join(map(str, range(i, 6))))

elif N == 8:
    for i in range(5, 0, -1):
        print(' ' * 8 + ' '.join(map(str, range(i, 6))))
    for i in range(1, 6):
        print(' ' * (10 - i * 2) + ' '.join(map(str, range(i, 0, -1))))

elif N == 9:
    for i in range(5, 0, -1):
        print(' '.join(['5'] * i))
    for i in range(1, 6):
        print(' '.join(['5'] * i))

elif N == 10:
    for i in range(1, 6):
        print(' ' * 8 + ' '.join(map(str, range(i, 0, -1))))
    for i in range(0, 6):
        print(' ' * (i * 2) + ' '.join(map(str, range(1, 6 - i))))
else:
    print("Введедо некоректне значення!!!")
