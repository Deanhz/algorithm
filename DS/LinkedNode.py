'''
LinkedNode algorithm
'''


class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


def create(l):
    head = ListNode()
    curNode = head
    for i in l:
        curNode.next = ListNode(i)
        curNode = curNode.next
    return head


def display(head):
    curNode = head.next
    while(curNode):
        print(curNode.val)
        curNode = curNode.next


class Solution(object):
    def delete_x(self, L, x):
        '''
        delete node that value equal x
        '''
        pre, p = L, L.next
        q = None
        while(p):
            if(p.val == x):
                q = p
                pre.next = p.next
                p = p.next
                del q
            else:
                pre = p
                p = p.next

    def reverse_print(self, L):
        if(L.next):
            self.reverse_print(L.next)
        print(L.val)

    def delete_min(self, L):
        pre, p = L, L.next
        minPre, minP = pre, p
        while(p):
            if(p.val < minP.val):
                minPre = pre
                minP = p
            pre = p
            p = p.next
        minPre.next = minP.next
        del minP

    def reverse_inplace(self, L):
        p = L.next
        L.next = None
        r = None
        while(p):
            r = p.next
            p.next = L.next
            L.next = p
            p = r

    def sorted_ascend(self, L):
        pre, p = L, L.next
        r = p.next
        p.next = None
        p = r
        while(p):
            r = p.next
            pre = L
            while(pre.next and pre.next.val < p.val):
                pre = pre.next
            p.next = pre.next
            pre.next = p
            p = r


if __name__ == '__main__':
    data = [1, 3, 2, 5, 4, 6]
    S = Solution()
    L = create(data)
    # algorithm test
    S.sorted_ascend(L)
    display(L)
