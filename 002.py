__author__ = 'pilagod'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    addone = False
    head = l1
    while(l2 is not None):
        l1.val = l1.val + l2.val + (1 if addone else 0)
        if l1.val >= 10:
            addone = True
            l1.val = l1.val - 10
        else:
            addone = False

        if l2.next is not None:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next

        l2 = l2.next

    while addone:
        if l1.next is None:
            l1.next = ListNode(0)
        l1 = l1.next
        l1.val = l1.val+1
        if l1.val >= 10:
            l1.val = l1.val - 10
            addone = True
        else:
            addone = False

    return head


l1 = ListNode(9)
l1.next = ListNode(8)

l2 = ListNode(1)

result = addTwoNumbers(l1, l2)
while result is not None:
    print(result.val)
    result = result.next