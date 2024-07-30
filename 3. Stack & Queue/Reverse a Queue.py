from math import floor
class queue:
    def __init__(self):
        self.q=[]
        self.front=-1
        self.rear=-1
    def enqueue(self, d):
        if self.front==-1 and self.rear==-1:
            self.front+=1
            self.rear+=1
            self.q.append(d)
        else:
            self.q.append(d)
            self.rear+=1
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("Underflow.......")
            return -1
        elif self.front==0 and self.rear==0:
            a = self.q.pop(self.front)
            self.rear-=1
            self.front-=1
        else:
            a = self.q.pop(self.front)
            self.rear-=1
        return a
    def traversal(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            tmp=self.front
            while(tmp<=self.rear):
                print(self.q[tmp],end=" ")
                tmp+=1
            print()
    def Isempty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False
    def reversal(self):
        if self.front==self.rear:
            return self.q
        else:
            start=self.front
            end=self.rear
            for i in range(0, floor((self.rear+1)/2)):
                temp=self.q[start]
                self.q[start]=self.q[end]
                self.q[end]=temp
                start+=1
                end-=1
            return self.q
               
               
MyQ=queue()
n=int(input())
while(n>=0):
  MyQ.enqueue(n)
  n=int(input())
if MyQ.Isempty():
  print("Queue is empty")
else:
  print("Before reversing:")
  MyQ.traversal()
  newQ=MyQ.reversal()
  print("After reversing:")
  MyQ.traversal()