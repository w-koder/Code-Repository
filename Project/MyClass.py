class MyClass:
    i = 10
    def f(self):
        self.i -= 1;
        print("before:" + (self.i + 1).__str__() + " after: " + self.i.__str__());
