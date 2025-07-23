# 🧭 O — Open/Closed Principle (OCP)

class Extractor:
    def extract(self, file_path):
        if file_path.endswith('.csv'):
            return self._read_csv(file_path)
        elif file_path.endswith('.xml'):
            return self._read_xml(file_path)
        # more elifs coming

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