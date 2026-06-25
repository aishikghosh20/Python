class vector_2d:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
class vector_3d(vector_2d):
    def __init__(self, length , width, height):
        super().__init__(length, width)
        self.height = height
    
    def __add__(self, other):
        return vector_3d(self.length + other.length, self.width + other.width, self.height + other.height)
    
    def __str__(self): # takes the class' object and returns a user-defined string 
        return f"{self.length}i + {self.width}j + {self.height}k"
    
a = vector_3d (10,5,12)
b = vector_3d (4,5,6)
c = vector_3d (7,8,9)

print(a + b)
print(a + c)
