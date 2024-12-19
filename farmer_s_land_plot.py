# Функция находит максимально возмозный размер квадрата на которые можно поделить участок

def main(width, height):
    if width == height:
        return f'Размер нужного квадрата {width} на {height}'
    if width % height == 0:
        return f'Размер нужного квадрата {height} на {height}'
    if height % width == 0:
        return f'Размер нужного квадрата {width} на {width}'
    else:
        if width > height:
            width = width % height
            return main(width, height)
        else:
            height = height % width
            return main(width, height)

if __name__ == "__main__":
    width = int(input('Введите ширину участка: '))
    height = int(input('Введите высоту участка: '))
    print(main(width, height))
