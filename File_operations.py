import os
from pathlib import Path
from os import strerror

path = Path(Path.home().joinpath("Desktop", "CSV", "Operations_file.txt"))
file_name = path

content = [1, 2, 3, 4, "six", "Eight", "Jan"]
content2 = ["Apples", "Mangoes", "Oranges"]
combined = content + content2
try:
    with open(file_name, mode="w+")as fl_obj:
        for item in combined:
            fl_obj.write(str(item)+"\n")
except OSError as err:
    print(f"An error occured: {strerror(err.errno)}")


