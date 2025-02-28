import redis

connection = redis.Redis(decode_responses=True)

cursor = '0'
while cursor != 0:
    cursor, keys = connection.scan(cursor=cursor)
    for key in keys:
        value = connection.get(key)
        print(f'Ключ: {key}, Значение: {value}')
