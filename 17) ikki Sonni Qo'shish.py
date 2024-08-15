class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(head1: Node, head2: Node) -> Node:
    dummy = Node()
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)

        current = current.next
        if head1: head1 = head1.next
        if head2: head2 = head2.next

    return dummy.next
