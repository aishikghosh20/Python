class employee:
    salary = 1200000
    @classmethod
    def show1(self):
        print(f"The original salary is {self.salary}") # value is not susceptible to instance values as this function is defined under class-method

    def show2(self):
        print(f"The new salary is {self.salary}") # value is susceptible to instance declaration of value

    @property # makes this function be treated as a class attribute
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o = employee()
o.salary =2500000
o.show1()
o.show2()
o.name = "Aishik Ghosh" 
print(o.fname)
print(o.lname)

    