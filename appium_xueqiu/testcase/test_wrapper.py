def extend(fuc):
    def hello(*args, **kwargs):
        print("hello")
        fuc(*args, **kwargs)
        print("good bye")
    return hello

@extend
def tmp():
    print("tmp")

@extend
def tmp1():
    print("tmp1")

def test_wrapper():
    tmp()
    tmp1()