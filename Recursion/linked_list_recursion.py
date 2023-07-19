import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
  if i < 0:     #invalid input handling
    return head #return head node for any negative number
  if head is None: #this would mean the linkedlist is empty or shorter than i
    return None    #return none to make no changes to list
  if i == 0:  #if i is 0, remove this node by removing pointers to it.
    return head.next_node  #removes current node by returning next node instead of current node.
  head.next_node = remove_node(head.next_node, i - 1) #recursive call to assign head.next_node
  return head #after i=0 node is removed, this return maintains pointers for all the other nodes
  
# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 2)
print(head.flatten())