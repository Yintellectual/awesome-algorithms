
#detect circle in directed graph
from typing import List




#detect circle in undirected graph
def detect_circle_undirected(graph, node, visited, parent):
    if node in visited:
        raise Exception("node should never be in visited")    
    
    visited.add(node)
    print(node)
    
    for child in graph[node]:
        if child not in visited:
            return detect_circle_undirected(graph, child, visited, node)
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

    
class DirectedGraphCircleDetector:
    def isCyclic(self, adj : List[List[int]]) -> bool : 
        visited = set()
        is_circle = set()
        for node in range(len(adj)):
            if node not in visited:
                is_circle = is_circle or self.detect_circle_directed(graph=adj, node=node, visited=visited,  ancestors=set())
        return is_circle
    
    def detect_circle_directed(self, graph, node, visited, ancestors):
        #if node in visited:
        #    raise Exception("node should never be in visited")    
        visited.add(node)
        ancestors.add(node)
        for child in graph[node]:
            if child in ancestors:
                return True
            else:
                #the child is not ancestor
                if self.detect_circle_directed(graph, child, visited, ancestors):
                    return True
        ancestors.remove(node)
        return False
    

if __name__ == "__main__":
    #graph = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
    #print(f"detect_circle: {detect_circle(graph=graph, node=0, visited=set(), parent=-1)}")
    #graph = [[1,2,3], [2,3,4], [3,4], [], [0, 3]]
    graph = [[1,3], [3], [4], [], []]
    detector = DirectedGraphCircleDetector()
    print(f"detect_circle: {detector.isCyclic(graph)}")