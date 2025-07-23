# 🧩 S — Single Responsibility Principle (SRP)

class ETLProcessor:
    def extract(self):
        # Connect to S3, read CSV
        pass
    def transform(self, data):
        # Clean, filter, enrich
        pass
    def load(self, data):
        # Insert into database
        pass