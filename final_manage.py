# manage_table.py
import os
from utils import *

def main():
    # Define the database file path
    db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'experiment.db')
    
    selected_table = None

    while True:
        tables = get_all_tables(db_path)
        print("\nSQLite Table Management Menu:")
        print("Available tables:")
        for table in tables:
            print(f" - {table}")
  
        print("1. Create Table with Columns")
        print("2. Delete Table")
        print("3. Select Table")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print()
            table_name = input("Enter name for the table: ")
            try:
                validate_table_name(table_name)
                num_columns = int(input("Enter number of columns: "))
                columns = []
                column_types = []
                for i in range(num_columns):
                    column_name = input(f"Enter name for column {i+1}: ")
                    column_type = input(f"Enter data type for column {i+1} (e.g., TEXT, INTEGER): ")
                    columns.append(column_name)
                    column_types.append(column_type)
                create_table_with_columns(db_path, table_name, columns, column_types)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            print()
            table_name = input("Enter name of the table to delete: ")
            try:
                delete_table(db_path, table_name)
                selected_table = None  # Deselect table after deletion
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            print()
            selected_table = select_table(db_path, tables)

            while selected_table:
                print("\nTable Management Menu:")
                print("1. View Table Contents")
                print("2. Insert Data into Table")
                print("3. Edit Table Data")
                print("4. Hitung Umur")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choice (1-5): ")

                if sub_choice == '1':
                    print()
                    view_table_contents(selected_table)
                elif sub_choice == '2':
                    print()
                    insert_data_into_table(selected_table)
                elif sub_choice == '3':
                    print()
                    edit_table_data(selected_table)
                elif sub_choice == '4':
                    print()
                    # Input tanggal mulai
                    mulai = input("Masukkan tanggal dengan format (tgl,bln,thn): ")
                    # Hitung umur
                    try:
                        umur = hitung(mulai)
                        print(f"Umur = {umur} hari")
                    except ValueError as e:
                        print(e)
                elif sub_choice == '5':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice == '4':
            print("Exiting SQLite Table Management Tool.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()