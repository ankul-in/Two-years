def a(x):
    def b(y):
        return x + y
    return b
print(f"{a(3)(4)}")

# from functools import partial

# def add(x: int):
#     return partial(x.__add)