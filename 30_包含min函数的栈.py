class StackWithMin(object):
    def __init__(self):
        self.real_stack = []
        self.min_stack = []

    def push(self, obj):
        assert isinstance(obj, (int, float))
        self.real_stack.append(obj)

        if not self.min_stack:
            self.min_stack.append(obj)
        else:
            self.min_stack.append(obj if obj < self.min_stack[-1] else self.min_stack[-1])

    def pop(self):
        if not self.real_stack or not self.min_stack:
            return None

        self.min_stack.pop()
        return self.real_stack.pop()

    def min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


if __name__ == "__main__":
    s = StackWithMin()
    s.push(2.98)
    s.push(3)
    print(s.real_stack)
    print(s.min())
    s.pop()
    print(s.real_stack)
    print(s.min())
    s.push(1)
    print(s.real_stack)
    print(s.min())
    s.pop()
    print(s.real_stack)
    print(s.min())
