letter = """Dear <Name>\nYou have been selected!!
<Date>"""
print(letter.replace("<Name>", input("Enter name : ").replace("<Date>", "!7.06.2026")))