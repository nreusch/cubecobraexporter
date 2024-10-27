# Cube Cobra MPC Exporter
This is a collection of scripts that can be used to download images from a cube on CubeCobra, including custom images.
The scripts also allow to format cards in an appropriate format for MakePlayingCards.

## downloadCubeImages
Given a .csv export from CubeCobra downloads all card images. Official images are downloaded from Scryfall in the correct version. Custom Images are downloaded via the image url given in the csv, if they are tagged with "custom".

Example:
```
python .\downloadCubeImages.py CustomSynergyCube.csv
```

## resizeImages
Uses ImageMagick (needs to be installed and on PATH) to modify card images for import into MakePlayingCards
- center_extent: Take image in size 745x1040 (Scryfall png default) and add a black border to it, necessary for MPC bleed
- crop: Crop 745x1040 image slightly to remove white corners
- scale: Scale a different sized image to 745x1040

Example:
```
python .\resizeImages.py center_extent doublesided
```

## flip_bit
Adds some random bytes to the end of all files in folder (Useful for tricking MPC to upload the same cardback multiple times)
```
python .\flip_bit.py cardback
```