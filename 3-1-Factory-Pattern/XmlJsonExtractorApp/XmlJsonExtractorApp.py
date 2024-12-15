from pathlib import Path
import json
import xml.etree.ElementTree as ET    

class JsonExtractor():
    def __init__(self, file_path_json: Path):
        self.data = {}
