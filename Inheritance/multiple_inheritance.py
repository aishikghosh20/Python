class employeee:
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} with a salary of {self.salary}")

class coder:
    def language(self,language):
        self.language = language

class programmer(employeee,coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The works in {self.company} with a proficiency in {self.language}")

a =employeee()
b = programmer()
b.language("Python")
b.show("Aishik",1200000)
b.showlanguage()
