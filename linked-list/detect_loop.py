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
    current = head
    if pos >= 1:
        i = pos
        while i >= 2:
            i -= 1
            current = current.next
        last.next = current
    return head

def detect_loop(head:Node) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    linked_list = linked_list_factory([1,2,3,4,5,6,7,8,9,10],6)
    print(detect_loop(linked_list))
        
