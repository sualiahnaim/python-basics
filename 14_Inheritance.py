class vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("Mileage of vehicle is ", self.mileage)
        print("Cost of vehicle is ", self.cost)
        print("I am a vehicle")

v1 = vehicle(500, 45000)
v1.show_vehicle_details()


class car(vehicle):
    def __init__(self, mileage, cost, hp):
        super().__init__(mileage, cost)   # parent class constructor call
        self.hp = hp                     

    def show_car_details(self):
        print("Mileage of car is ", self.mileage)
        print("Cost of car is ", self.cost)
        print("Horse Power of car is ", self.hp)
        print("I am a car")

c1 = car(250, 25000, 150)
c1.show_vehicle_details()
c1.show_car_details()
