import os
from os import strerror

file = "sring_frmting.py"
new_name = "string_frmting.py"
def rename(a, b):
    try:
        os.rename(file, new_name)
    except OsError as error:
        print(strerror(error.errorno))
    else:
        print(f"Renamed successfully: ")

if __name__ == "__main__":
    rename(file, new_name)
