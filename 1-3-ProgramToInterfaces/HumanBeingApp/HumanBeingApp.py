from abc import ABC, abstractmethod

class TonysExistentialCrisisBase(ABC):
    def __init__(self, name: str):
        self.name=name
        
    @abstractmethod
    def do_I_exist(self, am_i_alive: bool):
        pass
    
class MyHumanBeingClass(TonysExistentialCrisisBase):
    def do_I_exist(self, am_i_alive: bool=True):
        print("Cogito, ergo sum...👽")


def main():
    print("Welcome to HumanBeing App!")
    james = MyHumanBeingClass("James")
    james.do_I_exist()

if __name__ == "__main__":
    main()
