class Node:
  def __init__(self,d):
    self.data=d
    self.next=None
class main:
  def __init__(self):
    self.top=None
  def insert(self,d):
    newnode= Node(d)
    newnode.next=self.top
    self.top=newnode
  def traverse(self):
    temp=self.top
    while(temp is not None):
      print(temp.data,end=' ')
      temp=temp.next
      
obj= main()
d= int(input())
while(d>0):
  obj.insert(d)
  d=int(input())
obj.traverse()

  
