class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    return dummy.next