# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)
        even, odd = even_dummy, odd_dummy
        while head:
            if i%2 == 1:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
            i += 1
        odd.next = even_dummy.next
        even.next = None
        return odd_dummy.next


"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
