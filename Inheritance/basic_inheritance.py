class employeee:
    company = "ITC"
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} with a salary of {self.salary}")

class programmer(employeee):
    company = "ITC Infotech"
    # def show(self):
    #     print(f"The name is {self.name} with a salary of {self.salary}")
    # instead of wrting these again, inheritance is used, and all theattributes of 'employee' will be transfered to this class

    def showlanguage(self):
        print(f"The name is {self.name} with a proficiency in {self.language}")

a =employeee()
b = programmer()
print(b.show("Aishik",1200000))
