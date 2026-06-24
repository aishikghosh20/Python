class calc:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square is : {self.n * self.n}")

a= calc(4)
a.square()