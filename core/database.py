from core.table import Table

class Database:
    def __init__(self, name):
        self.name = name
        self.tables = {}  

    def create_table(self, name, columns, primary_key=None, unique_keys=None):
        """
        Create a table with optional primary key and unique keys
        """
        if name in self.tables:
            raise ValueError(f"Table '{name}' already exists")
        table = Table(name, columns, primary_key=primary_key, unique_keys=unique_keys)
        self.tables[name] = table
        print(f"Created table: {name}")
        return table

    def get_table(self, name):
        table = self.tables.get(name)
        if not table:
            raise ValueError(f"Table '{name}' does not exist")
        return table

    def show_tables(self):
        print(f"\nDatabase '{self.name}' tables:")
        for table_name in self.tables:
            print(f"- {table_name}")