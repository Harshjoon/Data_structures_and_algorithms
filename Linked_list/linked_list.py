class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        #self.next = None

    def __repr__(self):
        return "<Node data: %s>" % self.data
    

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add_data(self,data):
        new_node = Node(data)
        new_node.next_node = self.head.next_node
        self.head = new_node


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]"%current.data)
            if current.next == None:
                nodes.append("[Tail: %s]"%current.data)
            else:
                nodes.append("[%s]"%current.data)
            
            current = current.next_node

        return '->'.join(nodes)
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key: return current
            else: current = current.next_node
        return None
    
    def insert(self, data, index):
        if index == 0: self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position-=1

            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next


    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                self.head = current.next_node
                found = True
            if current.data == key:
                prev.next_node = current.next_node
                found = True
            else:
                prev = current
                current = current.next_node

        #return current


    def node_at_index(self, index):
        if index == 0: return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            
            return current

        


