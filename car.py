# --------------- car.py ---------------
class Car:
   def __init__(self, model, year, color, for_sale):
       self.model = model
       self.year = year
       self.color = color
       self.for_sale = for_sale

   def drive(self):
       # print("You drive the car")
       # print(f"You drive the {self.model}")
       print(f"You drive the {self.color} {self.model}")

   def stop(self):
       # print("You stop the car")
       # print(f"You stop the {self.model}")
       print(f"You stop the {self.color} {self.model}")

   def describe(self):
       print(f"{self.year} {self.color} {self.model}")
# --------------------------------------