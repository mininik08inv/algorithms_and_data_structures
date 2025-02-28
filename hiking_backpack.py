'''
задача о рюкзаке для похода
'''
items = {'water': {'weight': 3, 'cost': 10},
         'book': {'weight': 1, 'cost': 3},
         'food': {'weight': 2, 'cost': 9},
         'jacket': {'weight': 2, 'cost': 5},
         'camera': {'weight': 1, 'cost': 6}}

backpack_weight = 6

# Создаем таблицу для хранения данных
table = [[0 for _ in range(backpack_weight + 1)] for _ in range(len(items) + 1)]

# Заполняем таблицу
for i in range(1, len(items) + 1):
    for j in range(1, backpack_weight + 1):
        if items[list(items.keys())[i-1]]['weight'] <= j:
            table[i][j] = max(items[list(items.keys())[i - 1]]['cost'] + table[i - 1][j - items[list(items.keys())[i - 1]]['weight']], table[i - 1][j])
        else:
            table[i][j] = table[i - 1][j]

# Находим предметы, которые нужно положить в рюкзак
backpack = []
j = backpack_weight
for i in range(len(items), 0, -1):
    if table[i][j] != table[i - 1][j]:
        backpack.append(list(items.keys())[i-1])
        j -= items[list(items.keys())[i - 1]]['weight']

print('Предметы, которые нужно положить в рюкзак:', backpack)
