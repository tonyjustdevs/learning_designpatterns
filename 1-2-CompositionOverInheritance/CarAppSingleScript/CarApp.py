class Engine():
  def start(self):
    print("Engine started...🚗")

class Car():
  '''The Car class is composed of an Engine object:
  self.engine = Engine() allows for the 
  - engine to be easily swapped out
  - for another type 
  - without altering the Car class itself.
  '''
  def __init__(self):
      self.engine: Engine = Engine()
  
  def start(self):
      self.engine.start()
      print("Car started...🚗...")
      
def main():
  my_toyota_camry = Car()
  my_toyota_camry.start()

if __name__ == "__main__":
  main()
