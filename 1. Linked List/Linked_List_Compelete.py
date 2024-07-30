class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insertion at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    # Insertion at a random position (0-based index)
    def insert_at(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index out of range")
                return
            current = current.next
        
        if current is None:
            print("Index out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node
    
    # Deletion of first element
    def delete_first(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
    
    # Deletion of last element
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current
    
    # Deletion at a random position (0-based index)
    def delete_at(self, index):
        if self.head is None:
            return
        
        if index == 0:
            self.delete_first()
            return
        
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                print("Index out of range")
                return
            current = current.next
        
        if current.next is None:
            print("Index out of range")
            return
        
        current.next = current.next.next
        if current.next is None:
            self.tail = current
    
    # Reversing the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        if self.head is not None:
            self.tail = self.head
            while self.tail.next is not None:
                self.tail = self.tail.next

    # Printing the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Main execution
if __name__ == "__main__":
    linked_list = LinkedList()

    # Input values
    print("Enter numbers (enter a non-positive number to stop):")
    while True:
        n = int(input())
        if n <= 0:
            break
        linked_list.insert(n)
    
    print("\nOriginal list:")
    linked_list.print_list()

    # Insertion at random position
    index = int(input("\nEnter index to insert at: "))
    value = int(input("Enter value to insert: "))
    linked_list.insert_at(index, value)
    print("List after insertion:")
    linked_list.print_list()

    # Deletion at random position
    index = int(input("\nEnter index to delete from: "))
    linked_list.delete_at(index)
    print("List after deletion:")
    linked_list.print_list()

