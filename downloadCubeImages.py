import requests
from json import loads
import sys
from pathlib import Path
import time
import csv

# Given a .csv export from CubeCobra downloads all card images. Official images are downloaded from Scryfall in the correct version. Custom Images are downloaded via the image url given in the csv

headers_scryfall = {'User-Agent': 'NiklasCardDownloader', "Accept": "*/*"}
headers_imgur_etc = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

csv_reader = csv.reader(open(sys.argv[1], "r"), delimiter=',')
custom_tag = "custom"
custom_cards = {}
card_downloaded = 0
for row in csv_reader:
    c_name= row[0]
    if c_name != "name":
        # skip first line
        c_name = c_name.replace("/", "-")
        c_name = c_name.replace("\\", "-")
        c_set= row[4]
        c_set_nr= row[5]
        c_set_nr= c_set_nr.replace("★", "")
        maybeboard = row[10]
        image_url = row[11]
        tags = row[13]
        
        try:
            if maybeboard != "true":
                if custom_tag in tags:
                    print(f"{c_name} in custom cards. Downloading from CubeCubra Image URL")
                    r = requests.get(image_url, headers=headers_imgur_etc)

                    file_extension = image_url.split(".")[-1]
                    path = Path("custom") / Path(f"{c_name}.{file_extension}")
                    if path.is_file():
                        path = Path("custom") / Path(f"Duplicate_{c_name}.{file_extension}")
                    f = open(path, "wb")
                    f.write(r.content)
                    print(f"Custom: Created {path}")
                    f.close()
                else:
                    print(f"{c_name} {c_set} {c_set_nr}")
                    r = requests.get(f"https://api.scryfall.com/cards/{c_set}/{c_set_nr}", headers=headers_scryfall)
                    print(r.status_code)
                    scryfall_card = loads(r.text)
                    if not "image_uris" in scryfall_card:
                        if "image_uris" in scryfall_card["card_faces"][0]:
                            # double sided
                            img_url = scryfall_card["card_faces"][0]['image_uris']['png']
                            r = requests.get(img_url, headers=headers_scryfall)
                            
                            path = Path("doublesided") / f"Front_{c_name}.png"
                            f = open(path, "wb")
                            f.write(r.content)
                            print(f"Official: Created {path}")
                            f.close()
                            
                            img_url = scryfall_card["card_faces"][1]['image_uris']['png']
                            r = requests.get(img_url, headers=headers_scryfall)
                            
                            path = Path("doublesided") / f"Back_{c_name}.png"
                            f = open(path, "wb")
                            f.write(r.content)
                            print(f"Official: Created {path}")
                            f.close()
                        else:
                            raise("ERROR: No Image found on Scyfall")
                    else:
                        img_url = scryfall_card['image_uris']['png']
                        #print(scryfall_card)
                        r = requests.get(img_url, headers=headers_scryfall)
                        
                        path = Path("official") / f"{c_name}.png"
                        if path.is_file():
                            path = Path("official") / f"Duplicate_{c_name}.png"
                        f = open(path, "wb")
                        f.write(r.content)
                        print(f"Official: Created {path}")
                        f.close()
                card_downloaded += 1
                print()
        except Exception as e:
            raise(e)
            
        time.sleep(0.075)



# Get the image URL

print(f"Downloaded {card_downloaded} cards.")