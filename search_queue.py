from collections import  deque
import bfs

graph = {}
graph['cab'] = ['cat', 'car']
graph['car'] = ['cat', 'bar']
graph['cat'] = ['mat', 'bat', ]
graph['bar'] = ['bat']
graph['mat'] = ['bat']

# вызываем функцию поиска в ширину и выводим результат
print(bfs('cab', 'bat', graph))





