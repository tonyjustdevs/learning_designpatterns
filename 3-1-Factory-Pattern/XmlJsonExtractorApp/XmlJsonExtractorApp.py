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
