import csv
import os
from pathlib import Path

# Define the path to the desktop CSV folder
path = Path(Path.home().joinpath("Desktop", "CSV"))

# Check if the folder exists, if not, create it
if not os.path.exists(path):
    os.mkdir(path)

# Define the path to the CSV file
csv_file_path = path.joinpath("employees.csv")

# Check if the CSV file exists, if not, create it and write the header row
if  os.path.exists(csv_file_path):
    try:
        with open(csv_file_path, mode="w", newline="") as csv_file:
            emp_writer = csv.writer(csv_file, delimiter=",")
            emp_writer.writerow(["NAME", "DPT", "Age", "Date"])
    except OSError as err:
        print(f"Error: {err}")

# Function to add an employee to the CSV file
def add_Emp(name, dpt, age, year):
    try:
        with open(csv_file_path, mode="a", newline="") as csv_file:
            emp_writer = csv.writer(csv_file, delimiter=",")
            emp_writer.writerow([name, dpt, age, year])
    except OSError as err:
        print(f"Error: {err}")

# Call the add_Emp function to add an employee
add_Emp("Jeremy", "IT", 26, "04/03/2024")
add_Emp("John", "Engineering", 27, "06/03/2024")