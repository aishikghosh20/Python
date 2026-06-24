class programmer:
    company  = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p =programmer(input("Enter the name of the programmer:\n"), int(input("ENter the salary:\n")), int(input("ENter the employee pin:\n")))
print (p.company,p.name,p.salary,p.pin)
q =programmer(input("Enter the name of the programmer:\n"), int(input("ENter the salary:\n")), int(input("ENter the employee pin:\n")))
print (q.company,q.name,q.salary,q.pin)
r =programmer(input("Enter the name of the programmer:\n"), int(input("ENter the salary:\n")), int(input("ENter the employee pin:\n")))
print (r.company,r.name,r.salary,r.pin)