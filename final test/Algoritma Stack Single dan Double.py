
# Implementasi Stack Single dan Stack Double
# -----------------------------------------

# STACK SINGLE
class StackSingle:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return "Stack kosong"
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return "Stack kosong"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# STACK DOUBLE (dua stack dalam satu program)
class StackDouble:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push1(self, value):
        self.stack1.append(value)

    def push2(self, value):
        self.stack2.append(value)

    def pop1(self):
        return self.stack1.pop() if self.stack1 else "Stack 1 kosong"

    def pop2(self):
        return self.stack2.pop() if self.stack2 else "Stack 2 kosong"


# Contoh penggunaan
s1 = StackSingle()
s1.push(10)
s1.push(20)

print("Stack Single pop:", s1.pop())

sd = StackDouble()
sd.push1(1)
sd.push2(100)
print("Stack Double pop1:", sd.pop1())
print("Stack Double pop2:", sd.pop2())
