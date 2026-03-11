class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    #Poliformismo nos permite que subescrevemos um method que ya existe en tabla padre y
    #Adaptar para el hijo
    def move(self):
        print("Move!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Audi",1)
boat1 = Boat("Ibiza",2)
plane1 = Plane("Boeing",3)

for x in (car1,boat1,plane1):
    x.move()
