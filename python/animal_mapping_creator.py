import os
import re
import json
import uuid
from exiftool import ExifToolHelper

dict1 = {}

rootDir = '../frontend/assets/images'

with ExifToolHelper() as et:
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:

            fileLocation = dirName + "/" + fname
            fileLocation = fileLocation.replace("\\", "/")
            name = re.findall('\\\([a-z]+)', dirName.lower())

            obj = {"fileName": fname,
                "urlPath": "images/" + name[0] + "/" + fname,
                "dogName": name[0],
                }

            tags = et.get_tags([fileLocation], tags=["GPSLatitude", "GPSLongitude", "File:FileCreateDate", "File:ImageWidth", "File:ImageHeight"])[0]

            if "EXIF:GPSLatitude" in tags and type(tags["EXIF:GPSLatitude"]) == float:
                obj["gpsLatitude"] = tags["EXIF:GPSLatitude"]
            if "EXIF:GPSLongitude" in tags and type(tags["EXIF:GPSLongitude"]) == float:
                obj["gpsLongitude"] = tags["EXIF:GPSLongitude"]
            if "File:FileCreateDate" in tags and type(tags["File:FileCreateDate"]) == str:
                obj["fileCreationDate"] = tags["File:FileCreateDate"]
            if "File:ImageWidth" in tags and type(tags["File:ImageWidth"]) == int:
                obj["imageWidth"] = tags["File:ImageWidth"]
            if "File:ImageHeight" in tags and type(tags["File:ImageHeight"]) == int:
                obj["imageHeight"] = tags["File:ImageHeight"]
            
            dict1[str(uuid.uuid4())] = obj

with open("animal_mapping.json", "w") as f:
    f.write(json.dumps(dict1, indent=4))


# with ExifToolHelper() as et:
#     for d in et.get_metadata("../frontend/assets/images/atlas/20180616_135024.jpg"):
#         for k, v in d.items():
#             print(f"Dict: {k} = {v}")

    # for d in et.get_tags(["../frontend/assets/images/atlas/20180616_135024.jpg"], tags=["GPSLatitude", "File:FileCreateDate", "File:ImageWidth", "File:ImageHeight"]):
    #     for k, v in d.items():
    #         print(type(v))
    #         print(f"Dict: {k} = {v}")

# File:FileCreateDate
# File:ImageWidth
# File:ImageHeight