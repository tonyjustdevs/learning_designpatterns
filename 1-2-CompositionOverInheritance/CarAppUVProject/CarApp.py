class Engine():

  def start(self):
    print("Engine started...🚗")

class Car():
  def __init__(self) -> None:
      self.engine: Engine = Engine()
  
  def start(self):
      self.engine.start()
      print("Car started...🚗...")
        
def main():
  my_toyota_camry = Car()
  my_toyota_camry.start()

if __name__ == "__main__":
  main()
