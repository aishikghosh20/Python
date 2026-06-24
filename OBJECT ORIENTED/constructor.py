class employee: #class attribnutes
    language= "Hindi"
    salary = 120000

    def __init__(self, name, salary, language): # dunder method =>automatically called
        print("i am creating an obejct")
        self.name = name # these are creating instance attributes
        self.salary = salary
        self.language = language
    

emp1 = employee("harry", 150000, "English")
print(emp1.name,emp1.language,emp1.salary )

