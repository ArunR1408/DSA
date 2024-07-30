class TwoStacks:
    def __init__(self):
        self.array = [None] * 1000
        self.top1 = -1
        self.top2 = 1000

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = data
        else:
            print("Stack 1 is full")

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = data
        else:
            print("Stack 2 is full")

    def pop1(self):
        if self.top1 >= 0:
            self.array[self.top1] = None
            self.top1 -= 1
        else:
            print("Stack underflow. pop from stack 1 failed")

    def pop2(self):
        if self.top2 < 1000:
            data = self.array[self.top2]
            self.array[self.top2] = None
            self.top2 += 1
        else:
            print("Stack underflow. pop from stack 2 failed")

    def print_stack1(self):
        print("Stack 1 Elements:")
        for i in range(self.top1, -1, -1):
            print(self.array[i], end=" ")
        print()

    def print_stack2(self):
        print("Stack 2 Elements:")
        for i in range(self.top2, 1000):
            print(self.array[i], end=" ")
        print()


x = TwoStacks()
n1 = int(input())
a = input().split()
for i in a:
    if i.isdigit():
        x.push1(int(i))

n2 = int(input())
b = input().split()
for i in b:
    if i.isdigit():
        x.push2(int(i))

x.print_stack1()
x.print_stack2()

n3 = int(input())
for i in range(n3):
    x.pop1()

n4 = int(input())
for i in range(n4):
    x.pop2()

x.print_stack1()
x.print_stack2()