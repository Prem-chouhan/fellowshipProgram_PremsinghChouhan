class abc:

    def __init__(self):
        self.a = 12
        self.a =  13

    def dasd(self):
        print(self.a)

    def __del__(self):
        pass


obj = abc()
obj.dasd()
obj.a = 12543
print(obj.a)

class crud(abc):