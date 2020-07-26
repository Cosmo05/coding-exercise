#Nothing is here because i don't know about linked list ^_^
#defining Nodelist class
class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        self.data = data
        self.next = None
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False
#adding new node
def add(data): 
  
    newnode = node(0) 
    newnode.data = data 
    newnode.next = None
    return newnode 
  #ignore this i was trying to create a linked list
