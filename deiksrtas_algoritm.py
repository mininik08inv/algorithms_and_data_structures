import pprint

graph = {}
graph['start'] = {}
graph['start']['A'] = 2
graph['start']['B'] = 1
graph['start']['c'] = 1
graph['A'] = {}
graph['A']['E'] = 2
graph['A']['D'] = 5
graph['B'] = {}
graph['B']['E'] = 3
graph['B']['fin'] = 10
graph['C'] = {}
graph['C']['E'] = 3
graph['C']['fin'] = 9
graph['C']['D'] = 5
graph['E'] = {}
graph['E']['F'] = 1
graph['E']['fin'] = 6
graph['D'] = {}
graph['D']['fin'] = 3
graph['D']['F'] = 3
graph['D']['E'] = 1
graph['F'] = {}
graph['F']['fin'] = 4

graph['fin'] = {}

infinity = float('inf')
costs = {} # словарь в суммами которые складываются из весов всех ребер ведущих к узлу
costs['A'] = 2
costs['B'] = 1
costs['C'] = 1
costs['D'] = infinity
costs['E'] = infinity
costs['F'] = infinity
costs['fin'] = infinity

parents = {}
parents['start'] = None
parents['A'] = 'start'
parents['B'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs): # определяет узел с наименьшей стоимостью
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

parent = parents['fin']
while parent != None:
    print(parent + '  --->  ', end='')
    parent = parents[parent]