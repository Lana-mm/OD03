mas = [5, 7, 4, 3, 8, 2]
n = 6
for run in range(n-1):
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)

# Пузырьковая сортировка. Временная сложность: O(n²) в среднем и худшем случаях, O(n) в лучшем случае.
# Пространственная сложность: O(1).
