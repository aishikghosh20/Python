class employee: # claass attributes 
    language= "Hindi"
    salary = 120000
    def getinfo(self): # self parameter needed
        print(f"The lang is {self.language}. The salary is {self.salary}")

emp1 = employee()
emp1.language = "ENglish" # instance attribute
emp1.getinfo() # employee.getinfo(emp1) <--- same

