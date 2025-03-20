import random

# Размер массива
n = 10

# Генерация списка случайных чисел
array = [random.random() for _ in range(n)]

# Максимальное значение
max_value = max(array)

# Минимальное значение
min_value = min(array)

# Среднее значение
average_value = sum(array) / n

print(f"Сгенерированный массив: {array}")
print(f"Максимальное значение: {max_value:.4f}")
print(f"Минимальное значение: {min_value:.4f}")
print(f"Среднее значение: {average_value:.4f}")