class node:
  def __init__(self,data=None):
      self.data=data
      self.next=None
class link:
  def __init__(self):
      self.head=node()
  def append(self,data):
      nn=node(data)
      cur=self.head
      while cur.next!=None:
          cur=cur.next
      cur.next=nn
  def lis(self):
      l=[]
      cur=self.head
      cur=cur.next
      while cur.next!=None:
          print(int(cur.data))
          cur=cur.next
i=0
ll=link()
while i!=-1:
    i=int(input())
    ll.append(i)
ll.lis()

