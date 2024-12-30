# Быстрая сортировка
import random


def quick_sort(arr: list):
    # Если длинна массива меньше или равно 1, сортировать нечего, возвращаем исходный список
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент с помощью метода choice из библиотеки random
    mid = random.choice(arr)
    # Составляем подсписок из элементов которые меньше опорного
    list_smaller = [el for el in arr if el < mid]
    # Составляем подсписок из опорного элемента
    list_mid = [el for el in arr if el == mid]
    # Составляем подсписок из элементов которые больше опорного
    list_larger = [el for el in arr if el > mid]

    # Рекурсивно вызываем функцию quick_sort для каждого подмассива и возвращаем новый(отсортированный) список состоящий
    # из результатов работы вызванных функций
    return quick_sort(list_smaller) + list_mid + quick_sort(
        list_larger)


if __name__ == '__main__':
    arr = [3, 2, 7, 4, 1, 9, 55, 12, 1, 8]

    print(quick_sort(arr))
