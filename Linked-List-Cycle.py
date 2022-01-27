# Question Difficulty: Easy
# Question Number: 141
# Question URL: https://leetcode.com/problems/linked-list-cycle/

# NeetCode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        