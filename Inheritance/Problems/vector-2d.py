class vector_2d:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
class vector_3d(vector_2d):
    def __init__(self, length , width, height):
        super().__init__(length, width)
        self.height = height
    
    def show(self):
        print (f"The Volume is : {self.length * self.width * self.height}")

a = vector_3d(10,5,12)
a.show()
