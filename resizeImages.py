from pathlib import Path
import sys
import os

operation = sys.argv[1]
folder = sys.argv[2]

# Uses ImageMagick to modify card images for import into MakePlayingCards
# center_extent: Take image in size 745x1040 (Scryfall png default) and add a black border to it, necessary for MPC bleed
# crop: Crop 745x1040 image slightly to remove white corners
# scale: Scale a different sized image to 745x1040

if operation == "center_extent":
    pathlist = Path().glob(f"{folder}/*")
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)   
        print(path_in_str)
        os.system(f"magick \"{path_in_str}\" -gravity center -background black -extent 816x1110 \"{path_in_str}\"") 
elif operation == "crop":
    pathlist = Path().glob(f"{folder}/*")
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)   
        print(path_in_str)
        os.system(f"magick \"{path_in_str}\" -gravity Center -crop 700x995+0+0 +repage  \"{path_in_str}\"") 
elif operation == "scale":
    pathlist = Path().glob(f"{folder}/*")
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)   
        print(path_in_str)
        os.system(f"magick \"{path_in_str}\" -scale 745x1040! \"{path_in_str}\"") 