from constants import ELEMENT_RARITY_MAP

import json
import re
import urllib.request


TYPE = 0
ELEMENT = 1
RANK = 2
MIN_DAMAGE = 3
MAX_DAMAGE = 4

MEDIA_EXTENSION = "mp4"
NFT_EXTENSION = "json"
IMAGE_BASE_URL = "https://storage.googleapis.com/chordus-arena/media/"
NAME_PATTERN = "Ancient Artifact #"
EXTERNAL_URL = "https://www.chordusarena.com"
PREREVEAL_FILE_MEDIA = "Chordus_Arena_Logo.mp4"

class Metadata():
    id = 0
    rarity = 0
    meta  = {
        "description": "Chordus Arena is a collection of 3D deadly weapons that live on the Ethereum Blockchain and are ready to be held by the strongest Gladiators in the Arena. Each Ancient Artifact was manually hand-made to be absolutely stunning.",
        "image": IMAGE_BASE_URL,
        "name": NAME_PATTERN,
        "external_url": EXTERNAL_URL,
        "attributes": [
            ]
        }

    def __init__(self):
        self.meta = {
        "description": "Chordus Arena is a collection of 3D deadly weapons that live on the Ethereum Blockchain and are ready to be held by the strongest Gladiators in the Arena. Each Ancient Artifact was manually hand-made to be absolutely stunning.",
        "image": IMAGE_BASE_URL,
        "name": NAME_PATTERN,
        "external_url": EXTERNAL_URL,
        "attributes": [
            ]
        }
    
    def __del__(self):
        print("I'm being automatically destroyed. Goodbye!")

    def set_all_values(self, id, type, element, rank, min_damage, max_damage, stats):
        self.id = id
        self.meta["attributes"].append({"trait_type": "Type", "value": type})
        self.meta["attributes"].append({"trait_type": "Element", "value": element})
        self.meta["attributes"].append({"trait_type": "Rank", "value": rank})
        self.meta["attributes"].append({"trait_type": "MIN Damage", "value": int(min_damage)})
        self.meta["attributes"].append({"trait_type": "MAX Damage", "value": int(max_damage)})

        for stat in stats:
            self.meta["attributes"].append({"trait_type": stat[0], "value": int(stat[1])})     

        trp = self.calculate_trp()
        self.meta["attributes"].append({"trait_type": "TRP", "value": int(trp)})
        self.rarity = int(trp * ELEMENT_RARITY_MAP[element])
        self.meta["attributes"].append({"display_type": "number", "trait_type": "Rarity", "value": self.rarity})
        self.update_image_url()
        self.meta["name"] += str(id)

    def set_dummy_values(self, id):
        self.id = id
        self.meta["name"] += str(id)
        self.meta["image"] = IMAGE_BASE_URL + PREREVEAL_FILE_MEDIA
        return

    def extract_rarity(self):
        for attributes in self.meta["attributes"]:
            if attributes["trait_type"] == "Rarity":
                self.rarity = attributes["value"]
        return

    def set_rarity(self, rarity):
        for attributes in self.meta["attributes"]:
            if attributes["trait_type"] == "Rarity":
                attributes["value"] = rarity
                self.rarity = rarity

    def update_image_url(self):
        self.meta["image"] = IMAGE_BASE_URL + self.get_media_file_name()

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        self.set_name()

    #def get_rp(self):
    #    for attributes in self.meta["attributes"]:
    #        if attributes["trait_type"] == "TRP":
    #            print(self.meta["name"], attributes["value"])

    def set_name(self):
        self.meta["name"] = NAME_PATTERN + str(self.id)

    def get_name(self):
        return self.meta["name"]

    def set_element(self, element):
        self.meta["attributes"][ELEMENT]["value"] = element

    def generate_file_name(self, type, element, rank, extension):
        type = re.sub('[\s+]', '', type)
        return  type + '_' + element + '_' + rank + "." + extension

    def get_nft_file_name(self):
        return str(self.id) + "." + NFT_EXTENSION

    def get_media_file_name(self):
        return self.generate_file_name(self.meta["attributes"][TYPE]["value"], self.meta["attributes"][ELEMENT]["value"], self.meta["attributes"][RANK]["value"], MEDIA_EXTENSION)

    def save(self, file_name):
        rawJSON = json.dumps(self.meta, indent=4)
        print(rawJSON)
        a = open(file_name, 'w')
        a.write(rawJSON)
        a.close()
        return

    def get_min_damage(self):
        if(len(self.meta["attributes"]) < MAX_DAMAGE):
            raise NameError('Incomplete meta')
        return self.meta["attributes"][MIN_DAMAGE]["value"]

    def get_max_damage(self):
        if(len(self.meta["attributes"]) < MAX_DAMAGE):
            raise NameError('Incomplete meta')
        return self.meta["attributes"][MAX_DAMAGE]["value"]

    def read(self, file_name):
        f = open(file_name,'r')
        rawJSON = f.read()
        f.close()
        self.meta = json.loads(rawJSON)
        self.extract_rarity()
        #rawJSON = json.dumps(self.meta, indent=4)
        #print(rawJSON)
        #self.save("test.json", rawJSON)
        return

    def num_of_stats(self):
        return len(self.meta["attributes"]) - 7

    def calculate_trp(self):
        trp = self.get_max_damage()/5 + self.get_min_damage()/5
        I = range(5, len(self.meta["attributes"]))
        for i in I:
            trp += self.meta["attributes"][i]["value"]
            print("TRP: ", trp)
            print("Value: ", self.meta["attributes"][i]["value"])
        return trp

    def get_image_url(self):
        image_url = self.meta["image"]
        return image_url

    def verify_image_url(self):
        image_url = self.get_image_url()
        #print(self.get_name(), " ", image_url)
        try:
            with urllib.request.urlopen(image_url) as f:
                html = f.read()
        except:
            print("Exception: ", self.get_name(), " ", image_url)
        return


