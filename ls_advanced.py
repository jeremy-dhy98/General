import argparse
from pathlib import Path
import sys
import datetime

# Creating an arg parser
parser = argparse.ArgumentParser(prog="ls_advanced", description="This App lists \
        files in a given path/Directory.", epilog="Thanks for using %(prog)s.",)
        # argument_default="argparse.SUPPRES")
general = parser.add_argument_group("General output: ")#Create grped help for args
general.add_argument('path')

# Adding additional custom options(optional args)
detailed = parser.add_argument_group("detailed output: ")# Create grped help for optns
detailed.add_argument("-l", "--long", action="store_true")
args = parser.parse_args()  # Creating a namespace with commands and options
                            # The namespace allows you to access command and options
                            # using dot notation


target_dir = Path(Path.home().joinpath(args.path))

if not target_dir.exists():
    print('Target directory does not exist')
    sys.exit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp( entry.stat().st_mtime)\
                .strftime("%B %d %H:%M:%S")
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    # try:
    #     long = args.long
    # except AttributeError:
    #     long = False
    print(build_output(entry, long=args.long))
