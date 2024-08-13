class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow