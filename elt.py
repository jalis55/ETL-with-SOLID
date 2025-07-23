#  I — Interface Segregation Principle (ISP)

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



etl = ETLProcessor()
etl.run(MockExtractor())


class Extractable:
    def extract(self): pass

class Transformable:
    def transform(self): pass

class Loadable:
    def load(self): pass

class Notifiable:
    def notify(self): pass

class FileETLJob(Extractable, Transformable, Loadable):
    def extract(self):
        print("Extracting data from CSV")

    def transform(self):
            print("Transforming CSV data")

    def load(self):
        print("Loading data into DB")

class RealTimeETLJob(Extractable, Transformable, Notifiable):
    def extract(self):
        print("Extracting data from Kafka")

    def transform(self):
            print("Transforming real-time data")

    def notify(self):
        print("Notifying dashboard")



class ETLProcessor:
    def __init__(self):
        pass
  
    def run(self, job):
        job.extract()
        job.transform()

        if isinstance(job, Loadable):
            job.load()

        if isinstance(job, Notifiable):
            job.notify()
