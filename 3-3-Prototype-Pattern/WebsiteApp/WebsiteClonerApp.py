import copy 

class Web():
    def __init__(self, name = "default_name", 
                 domain="default_dom", 
                 desc="default_desc", 
                 **kwargs):
        self.name = name
        self.domain = domain
        self.desc = desc
        for key in kwargs:
            setattr(self, key, kwargs[key])
    def __str__(self):
        summary = [f"attr_name: {self.name:15} | attr_value {id(self)}\n"]
        
        infos_view = sorted(vars(self).items()) #some_dict
        
        for k,v in infos_view:
            if k=="name":
                continue
            summary.append(f"{f"attr_name: {k:15} | attr_value {v}"}\n")
        return "".join(summary)

class Prototype():
    def __init__(self):
        self.reg_dict = {}
    def register(self, uid: int, obj: object):
        self.reg_dict[uid] = obj
    def deregister(self, uid: int):
        del self.reg_dict[uid]
    def clone(self, uid:int, **attrs):
        object_found = self.reg_dict.get(uid)
        if not object_found:
            raise ValueError(f"Object not found! id[{uid!r}]")
        object_clone = copy.deepcopy(object_found)
        for key in attrs:
            setattr(object_clone,key,attrs[key])
        return object_clone
      

my_dict = {"a_key":"val_1","my_key": 2,"z_key": 666, "666":"reversed_val"}      
keywords_dict = {"keywords": ('python', 'programming', 'scripting', 'data', 'automation')}
kws = ('python', 'programming', 'scripting', 'data', 'automation')

site1 = Web(name = "Python", domain = "python.org", 
    desc = "Programming language ecosystem", 
    category = "Open Source Software",kws=kws,**keywords_dict)

protoyper = Prototype()
protoyper.register(id(site1), site1)
new_name = "Python Package Index"
new_desc = "new desc"
new_dom = "piepiepie.org"

my_dicty ={"another_key":99,
          "yet_another_key": 123}

site2 = protoyper.clone(id(site1))  
site3 = protoyper.clone(id(site1),name=new_name,desc=new_desc,domain=new_dom)
site4 = protoyper.clone(id(site1),name=new_name,desc=new_desc,domain=new_dom,**my_dicty)
print(site1)
vars(protoyper)
print(site2)
print(site3)
print(site4)
