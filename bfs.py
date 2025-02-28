from collections import deque



# graph = {
#     'A': ['M', 'C'],
#     'M': ['A', 'N'],
#     'N': ['M', 'B', 'P'],
#     'P': ['C', 'B', 'N'],
#     'B': ['P', 'N'],
#     'C': ['A', 'P'],
# }
graph = {}
graph['cab'] = ['cat', 'car']
graph['car'] = ['cat', 'bar']
graph['cat'] = ['mat', 'bat', ]
graph['bar'] = ['bat']
graph['mat'] = ['bat']

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    print(visited)
    return visited

start = 'cab'
goal = 'bat'
visited = bfs(start, goal, graph)

cur_node = goal
print(f'\npath from {goal} to {start}: \n {goal} ', end='')
while cur_node != start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node}', end='')
