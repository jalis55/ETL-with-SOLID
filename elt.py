# 🤝 L — Liskov Substitution Principle (LSP)

from abc import ABC, abstractmethod

class Extractor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> dict:
        pass

class CSVExtractor(Extractor):
    def extract(self, file_path: str) -> dict:
        with open(file_path, 'r') as f:
            data = f.read()
        return { 'data': data }

class MockExtractor(Extractor):
    def extract(self, file_path: str) -> dict:
        return { 'data': 'test' }


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

class ETLProcessor:
    def __init__(self):
        pass
  
    def run(self, extractor: Extractor):
        data = extractor.extract('data.csv')
        print("Extracted data:", data)


etl = ETLProcessor()
etl.run(MockExtractor())