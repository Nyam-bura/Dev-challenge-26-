class Table:
    def __init__(self, name, columns, primary_key=None, unique_keys=None):
        self.name = name
        self.columns = columns
        self.rows = []

        self.primary_key = primary_key
        self.unique_keys = unique_keys or []

        # Simple indexing for primary key and unique keys
        self.indexes = {}
        if primary_key:
            self.indexes[primary_key] = {}  
        for key in self.unique_keys:
            self.indexes[key] = {}

    def insert(self, row):
        # Check columns exist and validate types
        for col_name, col_type in self.columns.items():
            if col_name not in row:
                raise ValueError(f"Missing column: {col_name}")
            col_type.validate(row[col_name])

        # Enforce primary key
        if self.primary_key:
            pk_value = row[self.primary_key]
            if pk_value in self.indexes[self.primary_key]:
                raise ValueError(f"Primary key constraint violated: {self.primary_key}={pk_value}")

        # Enforce unique keys
        for key in self.unique_keys:
            value = row[key]
            if value in self.indexes[key]:
                raise ValueError(f"Unique constraint violated: {key}={value}")

        # Insert row
        self.rows.append(row)

        # Update indexes
        if self.primary_key:
            self.indexes[self.primary_key][row[self.primary_key]] = row
        for key in self.unique_keys:
            self.indexes[key][row[key]] = row

        print(f"Inserted row: {row}")

    def update(self, pk_value, updates):
        """Update a row by primary key"""
        if not self.primary_key:
            raise ValueError("Table has no primary key; cannot update by primary key")

        row = self.indexes[self.primary_key].get(pk_value)
        if not row:
            raise ValueError(f"No row found with {self.primary_key}={pk_value}")

        # Validate updates
        for col, val in updates.items():
            if col not in self.columns:
                raise ValueError(f"Column '{col}' does not exist")
            self.columns[col].validate(val)
            # Enforce unique keys if updating
            if col in self.unique_keys and val != row[col]:
                if val in self.indexes[col]:
                    raise ValueError(f"Unique constraint violated: {col}={val}")

        # Apply updates and update indexes
        for col, val in updates.items():
            # Remove old unique index
            if col in self.unique_keys:
                del self.indexes[col][row[col]]
            row[col] = val
            # Add new unique index
            if col in self.unique_keys:
                self.indexes[col][val] = row

        print(f"Updated row with {self.primary_key}={pk_value}: {row}")

    def delete(self, column, value):
        before_count = len(self.rows)
        remaining_rows = []
        for row in self.rows:
            if row.get(column) != value:
                remaining_rows.append(row)
            else:
                # Remove from indexes
                if self.primary_key:
                    self.indexes[self.primary_key].pop(row[self.primary_key], None)
                for key in self.unique_keys:
                    self.indexes[key].pop(row[key], None)
        self.rows = remaining_rows
        after_count = len(self.rows)
        print(f"Deleted {before_count - after_count} row(s) where {column}={value}")

    def search(self, column, value):
        # Return all rows where column == value
        if column in self.indexes:
            row = self.indexes[column].get(value)
            results = [row] if row else []
        else:
            results = [row for row in self.rows if row.get(column) == value]

        print(f"\nSearch results for {column}={value}:")
        for row in results:
            print(row)
        return results

    def show(self):
        print(f"\nTable: {self.name}")
        for row in self.rows:
            print(row)

    def inner_join(self,other_table,self_column,other_column):
        results = []
        for row_self in self.rows:
            value = row_self.get(self_column)
            for row_other in other_table.rows:
                if row_other.get(other_column) == value:
                    combined_row = {}
                    for k, v in row_self.items():
                        combined_row[f"{self.name}.{k}"] = v
                    for k, v in row_other.items():
                        combined_row[f"{other_table.name}.{k}"] = v
                    results.append(combined_row)
        print(f"\nInner join results ({self.name}.{self_column} = {other_table.name}.{other_column}):")

        for row in results:
            print(row)
        return results


# # core/table.py
# class Table:
#     def __init__(self, name, columns):
#         self.name = name
#         self.columns = columns  # dict: column_name -> type instance
#         self.rows = []

#     def insert(self, row):
#         # Check columns exist and validate types
#         for col_name, col_type in self.columns.items():
#             if col_name not in row:
#                 raise ValueError(f"Missing column: {col_name}")
#             col_type.validate(row[col_name])

#         self.rows.append(row)
#         print(f"Inserted row: {row}")

#     def show(self):
#         print(f"\nTable: {self.name}")
#         for row in self.rows:
#             print(row)

#     def delete(self, column, value):
#         """Delete rows where column == value"""
#         before_count = len(self.rows)
#         self.rows = [row for row in self.rows if row.get(column) != value]
#         after_count = len(self.rows)
#         print(f"Deleted {before_count - after_count} row(s) where {column}={value}")

#     def search(self, column, value):
#         """Return all rows where column == value"""
#         results = [row for row in self.rows if row.get(column) == value]
#         print(f"\nSearch results for {column}={value}:")
#         for row in results:
#             print(row)
#         return results


# core/table.py
