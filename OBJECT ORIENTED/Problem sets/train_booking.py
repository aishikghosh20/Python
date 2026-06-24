import random
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in trainn-no:{self.trainNo}, From: {fro}, To: {to}")
    def get_status(self):
        print(f"{self.trainNo}no Train is running successfully") 
    def get_fare(self,fro,to):
        print(f"""Ticket fare for train-no:{self.trainNo}, From: {fro} To: {to}
              is - {random.randint(222,555)}""")

t = train(11239)
t.book("Kolkata", "Delhi")
t.get_status()
t.get_fare("Kolkata", "Delhi")