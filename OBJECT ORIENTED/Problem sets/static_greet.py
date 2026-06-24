class method:
    def __init__(self, name):
        self.name =name
    @staticmethod
    def greet(): # will be  carried out without any parameter
        print("Hello there!!")

a = method("Aishik")
a.greet()