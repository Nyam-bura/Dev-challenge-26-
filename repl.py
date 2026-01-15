# repl.py
from core.database import Database
from core.types import Integer, Text

# Create a global database instance
db = Database("MiniDB")

def parse_command(cmd):
    """Basic command parser"""
    tokens = cmd.strip().split()
    if not tokens:
        return

    action = tokens[0].upper()

    try:
        if action == "CREATE":
            if tokens[1].upper() == "TABLE":
                table_name = tokens[2]
                # Simplified: columns in format: col:type (comma separated)
                cols_def = cmd[cmd.index("(")+1 : cmd.index(")")]
                columns = {}
                for col_def in cols_def.split(","):
                    name, type_str = col_def.strip().split(":")
                    if type_str.upper() == "INT":
                        columns[name] = Integer()
                    elif type_str.upper() == "TEXT":
                        columns[name] = Text()
                    else:
                        print(f"Unknown type: {type_str}")
                        return
                db.create_table(table_name, columns)
        elif action == "INSERT":
            # Format: INSERT INTO table VALUES val1,val2,...
            table_name = tokens[2]
            vals = cmd[cmd.index("(")+1 : cmd.index(")")].split(",")
            table = db.get_table(table_name)
            # Map values to columns order
            row = {}
            for col_name, val in zip(table.columns.keys(), vals):
                val = val.strip()
                # Convert INT if needed
                if isinstance(table.columns[col_name], Integer):
                    val = int(val)
                row[col_name] = val
            table.insert(row)
        elif action == "SELECT":
            table_name = tokens[3]
            table = db.get_table(table_name)
            table.show()
        elif action == "DELETE":
            table_name = tokens[2]
            table = db.get_table(table_name)
            # Simple WHERE col=val
            where_clause = cmd.upper().split("WHERE")[1].strip()
            col, val = [x.strip() for x in where_clause.split("=")]
            if isinstance(table.columns[col], Integer):
                val = int(val)
            table.delete(col, val)
        elif action == "UPDATE":
            table_name = tokens[1]
            table = db.get_table(table_name)
            set_part = cmd.upper().split("SET")[1].split("WHERE")[0].strip()
            col_to_set, new_val = [x.strip() for x in set_part.split("=")]
            where_clause = cmd.upper().split("WHERE")[1].strip()
            pk_col, pk_val = [x.strip() for x in where_clause.split("=")]
            if isinstance(table.columns[col_to_set], Integer):
                new_val = int(new_val)
            if isinstance(table.columns[pk_col], Integer):
                pk_val = int(pk_val)
            table.update(pk_val, {col_to_set: new_val})
        elif action == "JOIN":
            # Format: JOIN table1.table2 ON table1.col=table2.col
            parts = cmd.split()
            table1_name = parts[1]
            table2_name = parts[2]
            table1_col = parts[4].split("=")[0].split(".")[1]
            table2_col = parts[4].split("=")[1].split(".")[1]
            table1 = db.get_table(table1_name)
            table2 = db.get_table(table2_name)
            table1.inner_join(table2, table1_col, table2_col)
        elif action == "EXIT":
            print("Exiting REPL...")
            exit()
        else:
            print("Unknown command")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to MiniDB REPL! Type EXIT to quit.")
    while True:
        cmd = input("MiniDB> ")
        parse_command(cmd)

if __name__ == "__main__":
    main()
