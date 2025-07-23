# 🧩 S — Single Responsibility Principle (SRP)

class Extractor:
    def extract(self, file_path):
        print(f"Extracting data from {file_path}")
        return [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

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