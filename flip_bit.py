from pathlib import Path
import random
import sys

# Adds some random bytes to the end of all files in folder (Useful for tricking MPC to upload the same cardback multiple times)

folder = sys.argv[1]

pathlist = Path().glob(f"{folder}/*")
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)   
    print(path_in_str)
    with open(path, 'rb+') as f:
        f.seek(0, 2) # seek to end
        n = f.tell()
        
        nr = random.randint(0, 99999999)
        f.write(nr.to_bytes(4))