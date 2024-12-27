arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# Пузырьковая сортировка
bubble_sorted = arr.copy()
bubble_sort(bubble_sorted)
print("Отсортированный массив (пузырьковая сортировка):", bubble_sorted)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Быстрая сортировка
quick_sorted = quick_sort(arr.copy())
print("Отсортированный массив (быстрая сортировка):", quick_sorted)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# Сортировка выбором
selection_sorted = arr.copy()
selection_sort(selection_sorted)
print("Отсортированный массив (сортировка выбором):", selection_sorted)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Сортировка вставками
insertion_sorted = arr.copy()
insertion_sort(insertion_sorted)
print("Отсортированный массив (сортировка вставками):", insertion_sorted)