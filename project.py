class Vehicle:
    def __init__(self, vin, make, model, mileage):
        self.vin = vin
        self.make = make
        self.model = model
        self.mileage = mileage

    def get_maintenance_cost(self):
       
        return 50.0

    def display_info(self):
        return f"VIN: {self.vin} | {self.make} {self.model} | Mileage: {self.mileage} miles"



class Car(Vehicle):
    def __init__(self, vin, make, model, mileage, passenger_capacity):
        super().__init__(vin, make, model, mileage)
        self.passenger_capacity = passenger_capacity

    def get_maintenance_cost(self):
        
        return 50.0 + (5 * self.passenger_capacity)


class Truck(Vehicle):
    def __init__(self, vin, make, model, mileage, payload_capacity):
        super().__init__(vin, make, model, mileage)
        self.payload_capacity = payload_capacity

    def get_maintenance_cost(self):
       
        return 100.0 + (self.mileage * 0.01)



class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, mileage, has_sidecar=False):
        super().__init__(vin, make, model, mileage)
        self.has_sidecar = has_sidecar

    def display_info(self):
        base_info = super().display_info()
        if self.has_sidecar:
            return f"{base_info} (Sidecar Edition)"
        return base_info



class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def total_maintenance_report(self):
        print("=== FLEET MAINTENANCE REPORT ===")
        grand_total = 0.0

        for vehicle in self.vehicles:
            
            cost = vehicle.get_maintenance_cost()
            grand_total += cost
            print(f"{vehicle.display_info()} -> Maintenance Cost: ${cost:.2f}")

        print("-" * 40)
        print(f"Grand Total Maintenance Cost: ${grand_total:.2f}")



if __name__ == "__main__":
    
    car1 = Car(vin="C101", make="Toyota", model="Camry", mileage=15000, passenger_capacity=5)
    truck1 = Truck(vin="T201", make="Ford", model="F-150", mileage=50000, payload_capacity=3.0)
    moto1 = Motorcycle(vin="M301", make="Harley", model="Classic", mileage=8000, has_sidecar=True)

    
    my_fleet = Fleet()
    my_fleet.add_vehicle(car1)
    my_fleet.add_vehicle(truck1)
    my_fleet.add_vehicle(moto1)

 
    my_fleet.total_maintenance_report()