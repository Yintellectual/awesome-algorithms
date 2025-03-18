def detect_circle(graph, node, visited, parent):
    if node in visited:
        raise Exception("node should never be in visited")    
    
    visited.add(node)
    print(node)
    
    for child in graph[node]:
        if child not in visited:
            return detect_circle(graph, child, visited, node)
        elif child != parent:
            return True
    return False


def depth_first_search(graph, node, visited, parent):
    if node in visited:
        return True            
    
    visited.add(node)
    print(node)
    for child in graph[node]:
        if child not in visited:
            return depth_first_search(graph, child, visited, node)
        else:
            continue
    return False


def breadth_first_search(graph, node, visited, parent):
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        else:
            visited.add(current)
            print(current)
            for child in graph[current]:
                if child not in visited:
                    queue.append(child)
                else:
                    continue

if __name__ == "__main__":
    graph = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
    print(f"detect_circle: {detect_circle(graph=graph, node=0, visited=set(), parent=-1)}")
