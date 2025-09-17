class Foo:
    def bar(self):
        a = [1, 2, 3]  # the `a` variable only exists in this method
        self.baz = 'hello world'  # this assignment to self is now part of the Foo instance
        return a  # the `a` variable gets deleted at the end of the method, but the object it refers to is returned to the caller

foo = Foo()
x = foo.bar()  # `x` is now what `a` was in the method
print(x.baz)
print(foo.baz)