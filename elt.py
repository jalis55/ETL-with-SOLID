# 🧭 O — Open/Closed Principle (OCP)

class Extractor:
    def extract(self, file_path):
        raise NotImplementedError

class CSVExtractor(Extractor):
    def extract(self, file_path):
        # parse CSV
        pass

class XMLExtractor(Extractor):
    def extract(self, file_path):
        # parse XML
        pass

# Usage
extractors = [CSVExtractor(), XMLExtractor()]
for extractor in extractors:
    if extractor.can_handle(file_path):
        data = extractor.extract(file_path)
class Transformer:
    def transform(self, data):
        print("Transforming data")
        return [d for d in data if d["age"] > 26]

class Loader:
    def load(self, data):
        print(f"Loading data: {data}")

# Added coordination class to manage the ETL process
class ETLProcessor:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self, file_path):
        data = self.extractor.extract(file_path)
        transformed = self.transformer.transform(data)
        self.loader.load(transformed)