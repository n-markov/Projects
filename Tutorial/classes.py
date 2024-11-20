class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def moves(self):
        print("Moves along...")
    
    def get_make_model_year(self):
        return f"I'm a {self.year} {self.make} {self.model}"

class Airplane(Vehicle):
    def __init__(self, make, model, year, faa_id):
        super().__init__(make, model, year)
        self.faa_id = faa_id
        
    def moves(self):
        print("Flies along...")
    
    def get_make_model_year(self):
        return f"{super().get_make_model_year()} {self.faa_id}"

class Yacht(Vehicle):
    def moves(self):
        print("Sails along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna", "Skyhawk", 1980, "N-12345")
yacht = Yacht("Catamaran", "Lagoon", 2012)
golf_cart = GolfCart("Yamaha", "GC100", 2006)

vehicles = [cessna, yacht, golf_cart]
print("\n")

for vehicle in vehicles:
    print(vehicle.get_make_model_year())
    vehicle.moves()

