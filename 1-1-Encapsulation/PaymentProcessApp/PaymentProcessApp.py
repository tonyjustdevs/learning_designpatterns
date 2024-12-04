# - Create base class with static attribute and varying method
# - Create sub-classes with varied method

class PaymentBase():
  def __init__(self, amount: int):
    self.amount: int = amount
    
  def payment_method(self):
    pass
  
class CreditCard(PaymentBase):
  def payment_method(self):
    print(f"Credit Card Payment: {self.amount}")
  
class PayPal(PaymentBase):
  def payment_method(self):
    print(f"PayPal Payment: {self.amount}")
  
# tests
payments = [CreditCard(69), PayPal(420)]
for payment in payments:
  # print(payment.payment_)
  payment.payment_method()
  # print(payment.)