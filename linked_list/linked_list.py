class Node:

    def __init__(self, data:int):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

        
class LinkedList:
    def __init__(self, nodes_data:list=None):
        self.head = None
        
        if (isinstance(nodes_data,list) and len(nodes_data)!=0):
            temp = Node(nodes_data.pop(0))  # refer to expalnation1.txt
            self.head = temp
            
            for data in nodes_data:
                temp.next = Node(data)
                temp = temp.next
        elif isinstance(nodes_data,(int, float, complex)) :
            self.head = Node(nodes_data)
            
    def __repr__(self):
        node  = self.head
        nodes = []       # list of numerical values
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes) 

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    # methods defined are insert, delete, reverse
    
    def insert_first(self, node:Node): 
        node.next = self.head
        self.head = node
        
    def insert_last(self, node:Node):
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node
                


    def insert_after(self,  target_node_data:int, node:Node):
        if (self.head is None):
            print("INVALID OPERTION : use insert_last or insert_first instead")
            return

        for current_node in self:
            if (current_node.data == target_node_data):      # This requires all nodes to have non recurring values. Kinda lame :(
                temp = current_node.next                     # Or at least it will only act on first matched item
                current_node.next = node
                node.next = temp
                return
        print(f"Node with value {target_node_data} NOT FOUND")

    def delete(self, target_node_data):
        if (self.head is None):
            print("Linked List is empty")
            return
        if (self.head.data == target_node_data):
            temp = self.head
            self.head = self.head.next
            temp.next = None
            temp.data = None
            return
        for node in self:
            if(node.next.data == target_node_data):
                temp = node.next
                node.next = node.next.next
                temp.next = None
                temp.data = None
                return
        print(f"Node with value {target_node_data} NOT FOUND")

    def reverse(self, target_node_data = None):
        '''Tries to invert linked list at the target_node_data including itself.
        e.g. llist = 1 ->2 ->3 ->None
        reverse() gives 3 ->2 ->1 ->None
        reverse(2) gives 1 ->3 ->2 ->None'''
        save = None
        prev_node    = None
        if (target_node_data is not None):
            for node in self:
                if (node.next.data == target_node_data):
                    current_node = node.next
                    save = node
                    break

        else:
            current_node = self.head

        next_node = None       
        while(current_node is not None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node    = current_node
            current_node = next_node
            
        if (target_node_data is not None):
            save.next = prev_node

        else :
            self.head = prev_node

# main
llist = LinkedList([1,2,3,4])
print(llist)

llist.insert_after(2,Node(2.5))
print(llist)

llist.delete(2)
print(llist)

llist.reverse(3)
print(llist)
