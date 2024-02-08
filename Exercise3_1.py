# Згідно 9 варіанту
N = int(input("Введіть число від 1 до 9: "))
while N < 1 or N > 9:
    N = int(input("Введіть число від 1 до 9: "))
if 0 < N < 10:
    for i in range(N, 0, -1):
        print(' '.join(['#'] * i))
    for i in range(1, N + 1):
        print(' '.join(['#'] * i))
