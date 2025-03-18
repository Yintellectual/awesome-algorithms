class Node:
    def __init__(self, value):
        self.value = value
        self.next:Node = None

def linked_list_factory(values:list[int], pos: int = -1) -> Node:
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    last = current
    last.next = get_by_index_1_based(head, pos)
    return head

def get_by_index_1_based(head:Node, pos:int) -> Node:
    if pos < 1:
        return None

    current = head
    while current:
        if pos >= 1:
            pos -= 1
            current = current.next
        else:
            return current
    return None

def detect_loop(head:Node) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def remove_loop(head:Node) -> Node:
    visited = set()
    current = head
    while current.next:
        visited.add(current)
        if current.next in visited:
            current.next = None
            break
        current = current.next
    return head

def floyd_loop_removal(head:Node) -> Node:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if slow != fast:
        return head
    
    fast = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = None
    return head

    

if __name__ == "__main__":
    linked_list = linked_list_factory([1,2,3,4,5,6,7,8,9,10], -1)
    print(f"before: {detect_loop(linked_list)}")
    linked_list = floyd_loop_removal(linked_list)
    print(f"after: {detect_loop(linked_list)}")
        
