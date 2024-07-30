# Implementation of Linked List

class Node:
    def __init__(self,d): #__init__ - Constructor
        self.data = d
        self.next = None
        
class Main:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insertion 
    def insert(self,d):
        newN = Node(d)
        if (self.head == None):
            self.head = newN
            self.tail = newN
        else:
            self.tail.next = newN   
            self.tail = newN
    
    # Printing the created linked list
    def print(self):
        print(" ")
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print(" ")
        
    # Deletion of first element
    def del(self):
        if (self.next = None):
            self.head = self.head.next
    
    # Deletion of last element
    def del_last(self):
        temp = self.head
        while (temp.next.next != None):
            temp = temp.next



obj = Main() #IMP: Create object 

# Multiple input values
n = int(input("Enter the Input Numbers: "))
while (n > 0): # Input stops when n = neg value
    obj.insert(n)
    n = int(input())
    
obj.print()
