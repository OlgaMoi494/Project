int_number = int(input('Введите целое число: '))

total_cubes = 0
for i in range(1, int_number + 1):
    total_cubes += i ** 3
print(total_cubes)

total_cubes2 = 0
while int_number > 0:
    total_cubes2 += int_number ** 3
    int_number -= 1
print(total_cubes2)
