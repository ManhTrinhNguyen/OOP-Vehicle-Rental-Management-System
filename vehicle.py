class Vehicle:
  # Instances Attribute 
  def __init__(self, vehicle_id: int, make: str, model: str, year: int, rental_rate: float, available: bool) -> None:
    self.vehicle_id = vehicle_id
    self.make = make
    self.model = model
    self.year = year 
    self.rental_rate = rental_rate 
    self.available = available

  # Method Attribute
  def __str__(self) -> str:
    return f'Vehicle ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, year: {self.year}, rental_rate: {self.rental_rate}, available: {self.available}'

  def mark_rented(self): # Mark vehicle as rented (available to False)
    self.available = False 
    return f'Vehicle {self.model}: {self.make} rented'
  
  def mark_returned(self): # Mark vehicle as return (available to True)
    self.available = True 
    return f'Vehicle {self.model}: {self.make} returned'
  
