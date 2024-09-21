from vehicle import Vehicle

class Car(Vehicle): 
  # Instances Attribute 
  def __init__(self, vehicle_id: int, make: str, model: str, year: int, rental_rate: float, num_doors: int, available=True) -> None:
    super().__init__(vehicle_id, make, model, year, rental_rate, available)
    self.num_doors = num_doors

  
