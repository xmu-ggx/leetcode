
class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):

        prev, curr = None, head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev



if __name__ == '__main__':
    nodes = [LinkNode(i) for i in range(1,6)]
    head = nodes[0]

    for i in range(4):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = None
    
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


    res = Solution().reverseList(head)
    cur = res
    while cur:
        print(cur.val)
        cur = cur.next
