"""
There are no public and private class in python but it can be showed by _
class _className is private class
class className is public class
"""

class _Private:

    def __init__(self) -> None:
        pass

    def show():
        print("I am private")

class NotPrivate:

    def __init__(self) -> None:
        pass

    def show():
        print("I am not private")