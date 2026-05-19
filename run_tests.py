import os
import subprocess

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

result = subprocess.run(["pytest"])

if result.returncode == 0 and os.path.exists("test.db"):
    os.remove("test.db")