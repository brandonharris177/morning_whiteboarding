# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:


# def mergeTwoLists(self, l1: ListNode, l2: ListNode):
#     total_list = []
#     while l1.next != None:
#         total_list.append(l1)
#     while l2.next != None:
#         total_list.append(l2)

#     total_list.sort()
#     total_list.append(None)

#     solution = Solution()

#     count = 1
#     for value in total_list:
#         solution.add_next(value, total_list[count])
#         count += 1

#     return solution

###################################PROBLEM 1################################

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # should we copy the lists before doing anything
    # to them, or just mutate them directly? 
    
    # don't forget to check that the inputs are not None 
    
    # attach one of the lists to the end of the other list 
    # sort them 
    # Sorting incurs a runtime of O(n log n)
    # We wouldn't be able to use any built-in sorting methods 
    # So we'd have to implement it ourself 
​
    # What is the best possible we can achieve for this problem?
    # We traversed each list once? Can we do less work than that? 
    # O(n + m) is probably the best we can do as far as runtime is concerned 
    # Added each node to a new list 
    
    # Space complexity: We're creating an entirely new linked list to hold 
    # all of the values from our inputs lists
    # O(n + m) since we're copying each input ListNode 
    # Do we need to do this? 
    # Let's instead mutate one of the input lists 
    
    # init a new linked list 
    new_list = ListNode(None)
    # variable to keep track of where we are in the new list 
    current_new = new_list
    # keep track of the two current nodes, l1 and l2
    
    # traverse along both linked lists 
    while l1 is not None and l2 is not None:
        # compare the two values that l1 and l2 are referring to 
        # if l1.val == l2.val:
            # add both to our new list and increment both pointers 
        if l1.val <= l2.val:
            # take the smaller one and add it on to the end of a new linked list
            current_new.next = ListNode(l1.val)
            # update the new_list reference 
            l1 = l1.next
        else:
            current_new.next = ListNode(l2.val)
            l2 = l2.next
        current_new = current_new.next
            
    # once all of the nodes from one of the linked lists is added,
    # add all of the remaining nodes from the other list to the end of
    # the new linked list 
    # check l1 to see if it still has nodes 
    if l1 is not None:
        # add the rest of l1 to the end of our new list 
        current_new.next = l1
    # check l2 to see if it still has nodes 
    if l2 is not None:
        current_new.next = l2
        
    # return our new list - our initial dummy node 
    return new_list.next

    # Runtime for this strategy is O(n + m) where n and m are the lengths
    # of both linked lists 

###################################PROBLEM 2################################

 def hasCycle(self, head: ListNode) -> bool:
        # loop through the linked list 
        # look for the tail
            # if there is a tail, it's `next` is None 
            # how do we know when we've found the tail?
        
        # Idea 1: add a 'visited' property to each node as 
        # we traverse 
        # check to see if a node we're visiting has that 
        # property 
#         current = head 
        
#         while current is not None:
#             # check if the current node has the `visited` property
#             if hasattr(current, 'visited'):
#                 return True
            
#             current.visited = True
#             current = current.next 
#             # if we ever encounter a node with the 'visited', then
#             # we've been there before 
#             # or alternatively, set the `value` to None 
        
#         # we reached the end of the linked list 
#         return False
        
        # if we want to check the length of the list
        # how do we figure out the length? 
        # usually we'd figure out the length by traversing
        # until we got a node whose `next` is None
        # but if the linked list contains, we'd never get there 
        
        # What if we aren't allowed to mutate the linked list? 
        # Idea 2: Add the nodes to a set/hash table that keeps 
        # track of  nodes in the linked list we've visited 
        # as we traverse, we'll check if the current node 
        # is one we've visited before 
        # if it is, there must be a cycle, return True 
        
        # Idea 3: Traverse the linked list with two pointers,
        # one that moves at twice the speed of the other 
        # if there is a cycle in the list, then the faster 
        # runner will reach the end of the linked list 
        # otherwise, if there is a cycle, then the faster 
        # runner will lap the slower runner 
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            # increment the two pointers 
            fast = fast.next.next
            slow = slow.next 
            
            # check to see if they ever land on the same node 
            if fast is slow:
                return True
        
        # fast reached the end of the linked list 
		return False

#####################################Day 2 Problem 1####################################

