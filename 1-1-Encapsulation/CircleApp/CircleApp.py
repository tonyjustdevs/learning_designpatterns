
# add base class with _attribute to encapsulate #21
# add @property decorator to enable getter #22
# add @attribute.setter decorator to enable setter #23
# test: getter method invocation . #24
# test: setter method invocation = #25

class Circle(): # 21
  def __init__(self, name: str, radius: int):
    self.name: str = name
    self._radius: int = radius #21
  
  @property # 22
  def radius(self):
    return self._radius
  
  @radius.setter # 23
  def radius(self, new_radius):
    self._radius = new_radius
    # print(f"New radius: {self._radius}")``
  
  def __repr__(self):
    return f"Circle(name={self.name!r}, _radius={self._radius!r})"
  
circle = Circle("Sir Cumference",69)

print(circle)
print(circle.radius) #24
circle.radius=420 #25
print(circle.radius)

