from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database.")

class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB database.")

class DataProcessor:
    def _init_(self, database: Database):
        self.database = database

    def process_and_save(self, data):
        self.database.save(data)

processor = DataProcessor(MySQLDatabase())
processor.process_and_save("User Data")

processor = DataProcessor(MongoDBDatabase())
processor.process_and_save("User Data")