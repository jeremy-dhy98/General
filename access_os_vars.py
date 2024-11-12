import os
from pathlib import Path

path = Path(Path.cwd())
user_id = os.environ.get("ID")
print(user_id)
