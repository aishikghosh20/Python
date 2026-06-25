class employee:
    def __init__(self, salary):
        self.salary = salary
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary *(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, increment):
        self.increment =increment

a = employee(120000)
a.salaryAfterIncrement = 45
print(a.salaryAfterIncrement)