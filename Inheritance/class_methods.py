class employee:
    salary = 1200000
    @classmethod
    def show1(self):
        print(f"The original salary is {self.salary}") # value is not susceptible to instance values as this function is defined under class-method

    def show2(self):
        print(f"The new salary is {self.salary}") # value is susceptible to instance declaration of value


o = employee()
o.salary =2500000
o.show1()
o.show2()

    