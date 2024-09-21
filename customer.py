class Customer: 
  # Instances Atrribute 
  def __init__(self, customer_id: int, name: str, license_number: str) -> None:
    self.customer_id = customer_id
    self.name = name 
    self.license_number = license_number
    self.rented_vehicles = [] # List of vehicles currently rented by the customer (list of Vehicle objects).
    self.rental_history = [] # # Keeps track of all rented vehicles

  def rent_vehicle(self, vehicle): # Adds a vehicle to the customer's list of rented vehicles.
    if vehicle not in self.rented_vehicles: # If vehicle is not in the list 
      self.rented_vehicles.append(vehicle) 
      vehicle.mark_rented()
      return f'Added {vehicle} to the list'
    else :
      return f'Vehicle is already in the list'

  def return_vehicle(self, vehicle): # Removes a vehicle from the customer's rented vehicles.
     if vehicle in self.rented_vehicles:
       self.rented_vehicles.remove(vehicle)
       self.rental_history.append(vehicle) # After return add to rental history list 
       vehicle.mark_returned()
       return f'Returned {vehicle}'
     else:
       return f'Vehicle {vehicle} is not in the list'
     
  def view_rental_history(self):
    print(f'Rental history for {self.name}')
    for vehicle in self.rental_history:
      return (f"- {vehicle.make} {vehicle.model}")
    else :
      return (f"{self.name} has no rental history.")
     



  