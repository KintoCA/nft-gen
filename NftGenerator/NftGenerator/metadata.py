from constants import ELEMENT_RARITY_MAP

import json
import re

TYPE = 0
ELEMENT = 1
RANK = 2
MIN_DAMAGE = 3
MAX_DAMAGE = 4

MEDIA_EXTENSION = "mp4"
NFT_EXTENSION = "json"
IMAGE_BASE_URL = "https://test/"
NAME_PATTERN = "Chordus Arena Ancient Artefact #"

class Metadata():
    id = 0
    meta  = {
        "description": "Chordus Arena is a collection of unique, randomly generated collection of ancient artefacts on the Ethereum blockchain",
        "image": IMAGE_BASE_URL,
        "name": NAME_PATTERN,
        "external_url": "https://www.chordusarena.com",
        "attributes": [
            ]
        }

    def __init__(self):
        self.meta = {
            "description": "Chordus Arena is a collection of unique, randomly generated collection of ancient artefacts on the Ethereum blockchain",
            "image": "https://test/",
            "name": NAME_PATTERN,
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
        self.meta["attributes"].append({"display_type": "number", "trait_type": "Rarity", "value": int(trp * ELEMENT_RARITY_MAP[element])})
        file_name = self.generate_file_name(type, element, rank, MEDIA_EXTENSION)
        self.meta["image"] += file_name
        self.meta["name"] += str(id)

    
    def set_id(self, id):
        self.id = id
        self.set_name()

    def set_name(self):
        self.meta["name"] = NAME_PATTERN + str(self.id)

    def set_element(self, element):
        self.meta["attributes"][ELEMENT]["value"] = element

    def generate_file_name(self, type, element, rank, extension):
        type = re.sub('[\s+]', '', type).lower()
        return  type + '_' + element.lower() + '_' + rank.lower() + "." + extension

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
        #rawJSON = json.dumps(obj, indent=4)
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
