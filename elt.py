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
