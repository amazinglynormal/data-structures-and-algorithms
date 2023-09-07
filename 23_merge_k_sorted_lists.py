class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def mergeKLists(lists):
    if len(lists) == 0:
        return None

    k = []
    result = ListNode()
    k.append(result)

    all_empty = False

    while not all_empty:
        smallestValIndex = 0
        smallestVal = 0

        for i in range(len(lists)):
            all_empty = True
            if lists[i]:
                smallestValIndex = i
                smallestVal = lists[smallestValIndex].val
                all_empty = False
                break

        if all_empty:
            break

        for i in range(len(lists)):
            if lists[i] and lists[i].val < smallestVal:
                smallestVal = lists[i].val
                smallestValIndex = i

        a = lists[smallestValIndex]
        result.next = a
        result = result.next

        if a.next:
            lists[smallestValIndex] = a.next
        else:
            lists[smallestValIndex] = None

    return k[0].next


a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

lists = [a, b, c]

print(mergeKLists(lists))
