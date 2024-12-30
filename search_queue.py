from collections import  deque

graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph['bob'] = ["anuj", "peggy"]
graph['alice'] = ["peggy"]
graph['claire'] = ["thom", "jonny", "alice"]
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = ["maria"]

def person_is_saller(name: str):
    return True if 'maria' in graph[name] else False

def search(name: str):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    count = 0
    while search_queue:
        count += 1
        person = search_queue.popleft()
        if person not in searched:
            if person_is_saller(person):
                print(person + ' is friend Maria, searched for ' + str(count))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('В вашей сети нет друзей маши')
    return False



search('you')