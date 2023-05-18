import random

# Создаем кортеж из 10 случайных чисел от 0 до 3 включительно
t = tuple(random.randint(0, 3) for i in range(10))
print("Кортеж из 10 случайных чисел: ", t)

# Подсчитываем количество нулей в кортеже
zeros_count = t.count(0)
print("Количество нулей в кортеже: ", zeros_count)
