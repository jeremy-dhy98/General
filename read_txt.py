from File_operations import path

try:
    with open(path, mode="r+") as fl_obj:
        for line in fl_obj:
            print(line,  end=" ")
except (FileNotFoundError, PermissionError) as err:
    print(f"A{type(err).__name} has occured.")