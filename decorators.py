#custom decorators
def logTime(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@logTime
def greeting():
    print("Welcome")

greeting()