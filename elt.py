# 🤝 L — Liskov Substitution Principle (LSP)

class Extractor:
    def extract(self, file_path):
        raise NotImplementedError

class CSVExtractor:
    def extract(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

class MockExtractor:
    def extract(self, file_path):
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

# Added coordination class to manage the ETL process
class ETLProcessor:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self, extractor):
        data = extractor.extract('data.csv')
        print("Extracted data:", data)


etl = ETLProcessor()
etl.run(MockExtractor())