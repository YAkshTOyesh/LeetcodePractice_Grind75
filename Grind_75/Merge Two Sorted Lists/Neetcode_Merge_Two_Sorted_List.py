# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
      if list1.val < list2.val:
        tail.next = list1
        list1 = list1.next
      else:
        tail.next = list2
        list2 = list2.next
      tail = tail.next

    if list1:
      tail.next = list2
    if list2:
      tail.next = list1

    return dummy.next
    """
    Use dummy node technique for edge case. Space Complexity(1) No new memory is created !!!
    Just a pointer. Return as from dummy.next
    Then just grow the tail. The tail acts as a current.
    """
        

    