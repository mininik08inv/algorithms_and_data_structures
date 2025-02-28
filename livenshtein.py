from typing import List, Dict
import psycopg
import requests


def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def find_similar_items(input_abbr: str, items: List[Dict[str, str]]) -> List[Dict[str, str]]:
    min_distance = float('inf')
    similar_items = []

    for item in items:
        distance = levenshtein_distance(input_abbr, item[2])
        if distance < min_distance:
            min_distance = distance
            similar_items = [item]
        elif distance == min_distance:
            similar_items.append(item)

    return similar_items


# Пример использования
conn = psycopg.connect(dbname="lomportal", user="lomportal", password="071213", host="localhost", port="5432")
cursor = conn.cursor()

input_abbr = input("Введите аббревиатуру: ").upper()
cursor.execute("SELECT * FROM points_location WHERE abbreviation=%s", (input_abbr,))
point = cursor.fetchone()

if point:
    url = f'https://yandex.ru/navi?whatshere%5Bpoint%5D={point[4]}%2C{point[3]}&whatshere%5Bzoom%5D=16.768925&ll={point[4]}%2C{point[3]}&z=16.768925&si=e5wmhgefmj352468jpym3ewa4m'
    weather = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={point[3]}&longitude={point[4]}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

    print(f'''Запрашиваемый пункт: {point[2]}
                 \nАдрес: {point[1]}
                 \nКоординаты: {url}
                 \nНомер телефона: {point[-3]}
                 \nПогода в районе погрузки😄: температура воздуха : {weather.json()['current']['temperature_2m']}''')
else:
    cursor.execute("SELECT * FROM points_location")
    items = cursor.fetchall()
    similar_items = find_similar_items(input_abbr, items)

    if similar_items:
        print("Самые похожие варианты:")
        for point in similar_items:
            print(point[2], '-', point[1])
    else:
        print("Нет похожих вариантов.")

conn.close()
