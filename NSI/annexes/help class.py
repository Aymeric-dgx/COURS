class Test:
    def __init__(self, a = [0,1], b = [2,3]):
        self.a = a
        self.b = b
        self.c = "a"

    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def create(self):
        self.c = Test(self.get_a(), self.get_b())
    def set_a(self, a):
        self.a = Test(a)

    def get_c(self):
        return self.c
    
test = Test()
test.set_a([4,5])
d = test.get_a()
print(d)