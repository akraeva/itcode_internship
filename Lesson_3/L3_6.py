numb = int(input('Введите число: '))
status = True
i = 2
while status and i in range(numb // 2 + 1):
    if numb % i == 0:
        status = False
    i += 1
print('Простое' if status else 'Составное')
