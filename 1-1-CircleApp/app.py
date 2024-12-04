
# add base class with _attribute to encapsulate #21
# add @property decorator to enable getter #22
# add @attribute.setter decorator to enable setter #23
# test: getter method invocation . #24
# test: setter method invocation = #25

class Circle(): # 21
  def __init__(self, name: str, radius: int):
    self.name: str = name
    self._radius: int = radius #21
  

