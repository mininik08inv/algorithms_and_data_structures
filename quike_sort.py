# Быстрая сортировка
import random


def quick_sort(arr: list):
    # Если длинна массива меньше или равно 1, сортировать нечего, возвращаем исходный список
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент с помощью метода choice из библиотеки random
    support_element = random.choice(arr)
    # Составляем подсписок из элементов которые меньше опорного
    elements_are_smaller_than_the_reference_one = [el for el in arr if el < support_element]
    # Составляем подсписок из опорного элемента
    list_of_the_reference_element = [el for el in arr if el == support_element]
    # Составляем подсписок из элементов которые больше опорного
    elements_are_larger_than_the_reference_one = [el for el in arr if el > support_element]

    # Рекурсивно вызываем функцию quick_sort для каждого подмассива и возвращаем новый(отсортированный) список состоящий
    # из результатов работы вызванных функций
    return quick_sort(elements_are_smaller_than_the_reference_one) + list_of_the_reference_element + quick_sort(
        elements_are_larger_than_the_reference_one)


if __name__ == '__main__':
    arr = [3, 2, 7, 4, 1, 9, 55, 12, 1, 8]

    print(quick_sort(arr))
