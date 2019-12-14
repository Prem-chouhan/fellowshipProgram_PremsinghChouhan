class dummy:
    def __init__(self, foo):
        self.foo = foo

    def get_foo(self):
        return self.foo


my_dummy = dummy('blah')
dir(my_dummy)
