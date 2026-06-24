class employee: # class attributes 
    language= "Hindi"
    salary = 120000

emp1 = employee()
emp1.name = "harry" # object attribute , will not affect the class
emp1.language = "English" # instance attribute (gets more priority over class attributes)
print(emp1.name,emp1.language,emp1.salary )

