# utils.py
import sqlite3
from datetime import date
from table import Table

def count_days():
    """
    Calculates the number of days between two user-provided dates.
    Handles potential input errors and provides informative messages.
    """

    today = date.today()
    print(f"Today: {today.strftime('%d, %m, %Y')}")

    while True:
        try:
            start_input = input("Enter start date (DD,MM,YYYY): ")
            day, month, year = map(int, start_input.split(','))
            start_date = date(year, month, day)  

            end_input = input("Enter end date (DD,MM,YYYY): ")
            if end_input.strip() == "":
                end_date = today
            else:
                day, month, year = map(int, end_input.split(','))
                end_date = date(year, month, day) 

            if start_date > end_date:
                print("Start date cannot be after end date. Please try again.")
                continue

            break

        except ValueError:
            print("Invalid date format. Please enter dates in DD,MM,YYYY format separated by commas.")

    difference = end_date - start_date
    days = difference.days

    print(f"There are {days} days")

def get_all_tables(data_file):
    """
    Fetches all table names from the database, excluding those starting with 'sqlite' and 'android'.
    Args:
        data_file: The path to the database file.
    Returns:
        A list of table names.
    """
    try:
        with sqlite3.connect(data_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'android_%';")
            tables = [row[0] for row in cursor.fetchall()]
        return tables
    except Exception as e:
        print(f"Failed to retrieve table names: {e}")
        return []

def validate_table_name(table_name):
    """
    Validates the table name to ensure it is a valid SQL identifier.
    Args:
        table_name: The name of the table to validate.
    """
    if not table_name.isidentifier():
        raise ValueError("Invalid table name. Please enter a valid identifier.")

def create_table_with_columns(data_file, table_name, columns, column_types):
    """
    Creates a table with the specified name, columns, and data types.
    Args:
        data_file: The path to the database file.
        table_name: The name of the table to create.
        columns: A list of column names.
        column_types: A list of column data types.
    """
    try:
        column_definitions = [f"{col.strip()} {type_.strip()}" for col, type_ in zip(columns, column_types)]
        table = Table(data_file, table_name, column_definitions)
        print(f"Table '{table_name}' created successfully!")
    except Exception as e:
        print(f"Failed to create table: {e}")

def delete_table(data_file, table_name):
    """
    Deletes the specified table.
    Args:
        data_file: The path to the database file.
        table_name: The name of the table to delete.
    """
    try:
        table = Table(data_file, table_name)
        table.drop()
        print(f"Table '{table_name}' deleted successfully!")
    except Exception as e:
        print(f"Failed to delete table: {e}")

def select_table(data_file, tables):
    """
    Selects the specified table and returns the Table object.
    Args:
        data_file: The path to the database file.
        tables: A list of existing table names.
    Returns:
        The Table object if the table exists, None otherwise.
    """
    table_name = input("Enter name of the table to select: ")
    if table_name not in tables:
        print(f"Table '{table_name}' does not exist. Please select a valid table.")
        return None

    try:
        table = Table(data_file, table_name)
        print(f"Table '{table_name}' selected.")
        return table
    except Exception as e:
        print(f"Failed to select table: {e}")
        return None

def view_table_contents(table):
    """
    Displays the contents of the specified table.
    Args:
        table: The Table object.
    """
    if table is None:
        print("No table selected. Please select a table first.")
        return

    try:
        cursor = table.select_all()
        column_names = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        cursor.close()

        for row in results:
            for col_name, col_value in zip(column_names, row):
                print(f"{col_name}: {col_value}")
            print()  # Empty line between rows
        
        print("Table contents displayed successfully.")
    except Exception as e:
        print(f"Failed to display table contents: {e}")

def insert_data_into_table(table):
    """
    Inserts data into the specified table.
    Args:
        table: The Table object.
    """
    if table is None:
        print("No table selected. Please select a table first.")
        return

    try:
        cursor = table.select_all()
        column_names = [description[0] for description in cursor.description]
        cursor.close()

        data = input(f"Enter data values (comma separated) for columns ({', '.join(column_names)}): ")
        data_values = [value.strip() for value in data.split(',')]
        if len(data_values) != len(column_names):
            raise ValueError("Invalid number of data values. Please provide values for all columns.")

        table.insert(*data_values)
        print("Data inserted into table successfully.")
    except Exception as e:
        print(f"Failed to insert data into table: {e}")

def edit_table_data(table):
    """
    Edits data in the specified table.
    Args:
        table: The Table object.
    """
    if table is None:
        print("No table selected. Please select a table first.")
        return

    try:
        cursor = table.select_all()
        column_names = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        cursor.close()

        for idx, row in enumerate(results):
            print(f"{idx + 1}: {row}")

        row_number = int(input("Enter the row number to edit (starting from 1): "))
        if row_number <= 0 or row_number > len(results):
            raise ValueError("Invalid row number. Please enter a valid row number.")

        row_data = list(results[row_number - 1])  # Adjust for 0-based indexing
        row_id = row_data[0]  # Assuming the first column is the primary key

        for i, (column_name, value) in enumerate(zip(column_names, row_data)):
            new_value = input(f"Enter new value for column '{column_name}' (current value: '{value}'): ")
            if new_value:  # Only update if the user entered a new value
                row_data[i] = new_value

        set_args = {col: val for col, val in zip(column_names[1:], row_data[1:])}  # Exclude primary key from set_args
        where_args = {column_names[0]: row_id}

        table.update(set_args, **where_args)
        print("Row data updated successfully!")
    except Exception as e:
        print(f"Failed to edit table data: {e}")