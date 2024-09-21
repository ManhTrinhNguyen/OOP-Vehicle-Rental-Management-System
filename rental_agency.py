from rental_transaction import Rental_Transaction
from car import Car
from bike import Bike
from truck import Truck
from customer import Customer


class Rental_Agency:
  def __init__(self) -> None:
    self.vehicles = [] # A list of all vehicles in the rental agency (list of Vehicle objects).
    self.customer = [] # A list of registered customers (list of Customer objects).
    self.transactions = [] # A list of completed rental transactions (list of RentalTransaction objects).

  def register_customer(self, customer): # Registers a new customer with the rental agency.
    if customer not in self.customer: # If customer is not register  
      self.customer.append(customer)
      return f'{customer.name} with id : {customer.customer_id} has registered'
    else:
      return f'{customer.name} with id : {customer.customer_id} is already registered'
    
  def add_vehicle(self, vehicle): # Adds a new vehicle to the rental agency's fleet.
    if vehicle not in self.vehicles: # If vehicle is not in the list
      self.vehicles.append(vehicle)
      return f'{vehicle} has added to the list'
    else:
      return f'{vehicle} is already in the list'
    
  def rent_vehicle(self, customer, vehicle, rental_days, transaction_id): #  Rents a vehicle to a customer and creates a rental transaction.
    if vehicle in self.vehicles and vehicle.available:
      transaction = Rental_Transaction(transaction_id, customer, vehicle, rental_days)
      vehicle.mark_rented()
      customer.rent_vehicle(vehicle)
      self.transactions.append(transaction)
      return vehicle
    else :
      return (f"{vehicle.make} {vehicle.model} is not available.")
  
  def return_vehicle(self, customer, vehicle, transaction_id): # Returns a vehicle and completes the rental transaction.
    transaction = next((t for t in self.transactions if t.transaction_id == transaction_id), None)
    if transaction and not transaction.is_completed: 
      customer.return_vehicle(vehicle)
      return vehicle
    else : 
      return f"Transaction {transaction_id} could not be completed."
  
  def list_available_vehicles(self):
    for vehicle in self.vehicles:
      if vehicle.available: 
        print(vehicle)
    

# Create a rental agency
agency = Rental_Agency()

# Create some vehicles
car = Car(1, "Toyota", "Corolla", 2020, 40, num_doors=4)
bike = Bike(2, "Honda", "CBR", 2021, 25, type_of_bike="Sport")
truck = Truck(3, "Ford", "F-150", 2019, 80, cargo_capacity=2.0)

# Add vehicles to the agency
agency.add_vehicle(car)
agency.add_vehicle(bike)
agency.add_vehicle(truck)

# Register a customer
customer = Customer(1, "John Doe", "D1234567")
print(agency.register_customer(customer))

# List available vehicles
# print("\nAvailable vehicles:")
# agency.list_available_vehicles()
print(agency.list_available_vehicles())

# Rent a car
print(agency.rent_vehicle(customer, car, rental_days=3, transaction_id=101))


# Return the car
print(agency.return_vehicle(customer, car, transaction_id=101))

