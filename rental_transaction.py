class Rental_Transaction: 
  def __init__(self, transaction_id: int, customer, vehicle, rental_days: int, rental_date) -> None:
    self.transaction_id = transaction_id
    self.customer = customer # The customer involved in the transaction (Customer object).
    self.vehicle = vehicle # The vehicle involved in the transaction (Vehicle object).
    self.rental_days = rental_days
    self.rental_date = rental_date
    self.return_date = None 
    self.total_cost = self.calculate_cost() 
    self.is_completed = False 
    self.late_fee = 0
    self.discount = 0


  def calculate_cost(self): #  Calculates the total cost of the rental based on the vehicle's daily rate and the number of rental days.
    total_cost = self.vehicle.rental_rate * self.rental_days
    # # Apply 10% discount for rentals longer than 7 days
    if self.rental_days > 7:
      self.discount = 0.1 
      total_cost *= 1 - self.discount
    return total_cost
  
  def calculate_late_fee(self, actual_return_date): #
    rental_period = self.rental_days
    actual_rental_period = (actual_return_date - self.rental_date).days 

    if actual_rental_period > rental_period:
      # Apply 15% late fee daily 
      extra_days = actual_rental_period - rental_period
      self.late_fee = extra_days * (self.vehicle_rental_rate * 0.15)
    return self.late_fee

  def complete_transaction(self): # Marks the transaction as completed and updates vehicle availability.
    self.is_completed = True 
    self.vehicle.mark_returned()
    return f"Transaction {self.transaction_id}: {self.customer.name} rented {self.vehicle.make} {self.vehicle.model} for {self.rental_days} days. Total cost: ${self.total_cost}"
  

