from pathlib import Path
import sys

if (args_count := len(sys.argv)) > 2: # App should'nt accept more than 2 target dirs
    print(f"Expected a single argument, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory.")
    raise SystemExit(2)
target_dir = Path(Path.home().joinpath(sys.argv[1]))

if not target_dir.is_dir():
    print("Tatget directory not found", target_dir)
    raise SystemExit(1)
for entry in target_dir.iterdir():
    print(entry.name)