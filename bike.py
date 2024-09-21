from vehicle import Vehicle

class Bike(Vehicle):
  def __init__(self, vehicle_id: int, make: str, model: str, year: int, rental_rate: float, type_of_bike: str, available: bool) -> None:
    super().__init__(vehicle_id, make, model, year, rental_rate, available)
    self.type_of_bike = type_of_bike

    

