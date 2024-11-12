import argparse
from pathlib import Path
import sys

# Creating an arg parser
parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()  # Creating a namespace with commands and options
                            # The namespace allows you to access command and options
                            # using dot notation

target_dir = Path(Path.home().joinpath(args.path))

if not target_dir.exists():
    print('Target directory does not exist')
    sys.exit(1)

for entry in target_dir.iterdir():
    print(entry.name)
