from vehicle import Vehicle

class Truck(Vehicle): 
  def __init__(self, vehicle_id: int, make: str, model: str, year: int, rental_rate: float, cargo_capacity: float, available=True) -> None:
    super().__init__(vehicle_id, make, model, year, rental_rate, available)
    self.cargo_capacity = cargo_capacity 


  