import os
import shutil
from pathlib import Path

def cleanup_local_excgrouper_storage():
    local_storage_path = os.path.expanduser("~/.excgrouper")
    
    if Path(local_storage_path).exists():
        try:
            shutil.rmtree(local_storage_path)
            print(f"Successfully removed local storage at {local_storage_path}")
        except Exception as e:
            print(f"Error while removing local storage at {local_storage_path}: {e}")
    else:
        print(f"No local storage found at {local_storage_path}")

if __name__ == "__main__":
    cleanup_local_excgrouper_storage()