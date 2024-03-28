class ParkingSystem:
    def __init__(self, parking_size):
        self.parking_size = parking_size
        self.parking_spaces = {i: None for i in range(1, parking_size + 1)}
        self.parked_cars = {}
def park_car(self, car_plate, parking_space):
        if parking_space not in self.parking_spaces or self.parking_spaces[parking_space] is not None:
            return "Error: Parking space is already occupied or does not exist."

        self.parking_spaces[parking_space] = car_plate
        if car_plate not in self.parked_cars:
            self.parked_cars[car_plate] = 0
        self.parked_cars[car_plate] += 1

        return f"Car {car_plate} has been parked in space {parking_space}."

    def unpark_car(self, car_plate, parking_space):
        if parking_space not in self.parking_spaces or self.parking_spaces[parking_space] != car_plate:
            return "Error: Car is not parked in this parking space."

        self.parking_spaces[parking_space] = None
        self.parked_cars[car_plate] -= 1
        if self.parked_cars[car_plate] == 0:
            self.parked_cars.pop(car_plate)

        return f"Car {car_plate} has left the parking space {parking_space}."

    def get_car_parking_duration(self, car_plate):
        if car_plate not in self.parked_cars:
            return "Error: Car is not parked in the parking lot."

        return self.parked_cars[car_plate]

# Example usage
parking_system = ParkingSystem(5)
print(parking_system.park_car("ABC123", 1))
print(parking_system.park_car("DEF456", 2))
print(parking_system.get_car_parking_duration("ABC123"))
print(parking_system.unpark_car("ABC123", 1))
print(parking_system.get_car_parking_duration("ABC123"))