import csv
from pathlib import Path

# Define the path to the desktop CSV folder and the CSV file
path = Path(Path.home().joinpath("Desktop", "CSV").joinpath("employees.csv"))

def read_csv():
    with open(path, newline='', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', lineterminator="\t\t")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f"Column names/Field names: {', '.join(row)}")
                line_count += 1
            else:
                print(f"\t{row[0]} works in {row[1]} department and is aged {row[2]}.")
                line_count += 1
        print(f"Processed {line_count} lines.")

read_csv()
