def singleton(class_name):
    _instances = {}

    # *args, **kwargs要写在里面才work
    def get_instance(*args, **kwargs):
        if class_name not in _instances:
            _instances[class_name] = class_name(*args, **kwargs)
        return _instances[class_name]

    return get_instance


@singleton
class MyClass(object):
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(self.x, self.y, self.z)
        print("id: %s" % id(self))
        print()


if __name__ == "__main__":
    m1 = MyClass(4, 5, 6)
    m1.display()
    m2 = MyClass(1, 2)
    m2.display()
