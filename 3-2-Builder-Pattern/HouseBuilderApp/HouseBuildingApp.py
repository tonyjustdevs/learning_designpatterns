class HouseBuilder():
    def __init__(self):
        self.storeys: int|None = None
        self.has_ac: bool|None = None
        self.floor_type: str|None = None
    
    def set_storeys(self, storeys: int|None):
        self.storeys = storeys
        return self
    
    def set_has_ac(self, has_ac: bool|None):
        self.has_ac = has_ac
        return self
    
    def set_floor_type(self, floor_type: str|None):
        self.floor_type = floor_type
        return self

    def build(self):
        house = House(self) # House() to be implemented
        self.__init__() # reset attrs to None for next build()
        return house    # to be passed to House()   

    def __str__(self):
        return f"Hi, I'm a builder of houses 🏚️!"
# - 2a.     HouseBuilderCls:  
# - 2bi.    init(self)    
# - 2bii.    obj_attrs: .storeys, .has_ac, .floor_type    
# - 2biii.   obj_attrs assign to None  
# - 2c.     obj_method: set_obj_attrs(self, value) for all attrs  
# - 2d.     obj_method: build(self): return House(self)       

class House():
    def __init__(self, builder: HouseBuilder):
        self.storeys: int|None = builder.storeys
        self.has_ac: bool|None = builder.has_ac
        self.floor_type: str|None = builder.floor_type

    def __str__(self):
        return  (
            f"A {self.storeys}-storey house "
            f"with {self.floor_type} floors "
            f"{'and with' if self.has_ac else 'but without'} aircon "
            )
# - 1a.     HouseCls    
# - 1bi.    init(self, HouseBuilder)    
# - 1bii.     obj_attrs: .storeys, .has_ac, .floor_type  
# - 1biii.    obj_attrs assign to HouseBuilder_obj_attrs  

# test 1 - single storey house - no director
builder_1 = HouseBuilder()
sgl_stry_hs = builder_1\
    .set_storeys(1)\
    .set_has_ac(None)\
    .set_floor_type("wooden")\
    .build()

# test 2 - double storey house - no director
dbl_stry_hs = builder_1\
    .set_storeys(2)\
    .set_has_ac(True)\
    .set_floor_type("tile")\
    .build()
    
print(sgl_stry_hs)
print(dbl_stry_hs)

class Director():
    def __init__(self, builder: HouseBuilder):
        self.builder: HouseBuilder = builder
    
    def build_single_storey_house(self):
        house = self.builder\
            .set_storeys(1)\
            .set_has_ac(None)\
            .set_floor_type("wooden")\
            .build()
        return house

    def build_two_storey_house(self):
        house = self.builder\
            .set_storeys(2)\
            .set_has_ac(True)\
            .set_floor_type("tile")\
            .build()
        return house
     
    def __str__(self):
        return "Hi, I'm a director of house builders 🏗️!"
      
builder_1 = HouseBuilder()
print(builder_1)
director_1 = Director(builder_1)
print(director_1)

single_storey_house_d1 = director_1.build_single_storey_house()
print(single_storey_house_d1, [id(single_storey_house_d1)])

double_storey_house_d1 = director_1.build_two_storey_house()
print(double_storey_house_d1, [id(double_storey_house_d1)])

single_storey_house_d1 = director_1.build_single_storey_house()
print(single_storey_house_d1, [id(single_storey_house_d1)])

single_storey_house_d1 = director_1.build_single_storey_house()
print(single_storey_house_d1, [id(single_storey_house_d1)])

double_storey_house_d1 = director_1.build_two_storey_house()
print(double_storey_house_d1, [id(double_storey_house_d1)])
