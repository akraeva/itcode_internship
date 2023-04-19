n = int(input('Порядковый номер числа:'))
if n in (1, 2):
    result = 1
else:
    prev_num = 1
    next_num = 1
    for i in range(n-2):
        result = prev_num + next_num
        prev_num = next_num
        next_num = result
print(f'{n} число Фибоначчи равно {result}')
