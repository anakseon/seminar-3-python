N = int(input('Введите количество элементов списка: '))
var = [1, N]
X = int(input('Введите число X, которое необходимо найти в списке: '))
min = X
index = 0
for i in range(1, N):
    count = X - N[i]
    if count < min:
        min = count
        index = i
print(f'Число {N[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {X - N[index]}')
