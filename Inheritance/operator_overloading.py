class numbers:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, other):
        return self.n + other.n
    
    def __mul__(self, other):
        return self.n * other.n
    
n= numbers(4)
m= numbers(3)
print(n*m)
print(n+m)