marks = {
    "Harry":56,
    "Shubham": 76,
    "Rohan":23,
    "Jojo": 89,
    "Aishik": 95,
    12: "Bhanu"
}
print(marks, type(marks))

# TO invoke an element
print(marks["Harry"])
print(marks["Aishik"])

# TO print all the items
print(marks.items())

# Keys
print(marks.keys())

# Values
print(marks.values())

# Mutability
marks.update({"Harry": 99, "Renu": 45}) 
print(marks)

# To get an individual value
print(marks.get("Harry"))
print(marks["Harry"])  # if key is incorrect , returns an error

