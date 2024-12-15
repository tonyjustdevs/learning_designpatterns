from pathlib import Path
import json
import xml.etree.ElementTree as ET    

class JsonExtractor():
    def __init__(self, file_path_json: Path):
        self.data = {}
        with open(file_path_json) as f:
            self.data = json.load(f)
    @property
    def parsed_data(self):
        return self.data
    
class XmlExtractor():
    def __init__(self, file_xml_PATH: Path):
        self.tree = ET.parse(source=file_xml_PATH)
    @property
    def parsed_data(self):
        return self.tree
      
      
import os

project_dir_STR = os.getcwd() # 1.  get project root directory

# 2.  get data file paths
movies_json_PATH = project_dir_STR/Path("movies.json") # 2a. movies json path

person_xml_relo_PATH = project_dir_STR/Path("person.xml") # 2b. person xml path

movies_json_INSTANCE = JsonExtractor(movies_json_PATH) # 3. create data instances
person_xml_INSTANCE = XmlExtractor(person_xml_relo_PATH)

def data_extractor_factory(file_path: Path):
    ext = file_path.name.split(".")[-1] # json or xml
    
    if ext == 'json':
        print("processing json")
        return JsonExtractor(file_path)
    elif ext == 'xml':
        print("processing xml")
        return XmlExtractor(file_path)
    else:
        raise ValueError(f"Do not compute 🤖 .{ext!r}")

movies_factory_json_INSTANCE = data_extractor_factory(movies_json_PATH)
data_list = movies_factory_json_INSTANCE.parsed_data
print(data_list[0])

person_factory_xml_INSTANCE = data_extractor_factory(person_xml_relo_PATH)
print(person_factory_xml_INSTANCE.parsed_data.getroot())

# Test: Unexpected extension 'txt'
data_instance = data_extractor_factory(file_path=project_dir_STR/Path("yolo.txt")) # Expected: ValueError
