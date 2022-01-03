import json
import re

TYPE = 0
ELEMENT = 1
RANK = 2
MIN_DAMAGE = 3
MAX_DAMAGE = 4

class Metadata():

    meta  = {
        "description": "Chordus Arena is a collection of unique, randomly generated collection of ancient artefacts on the Ethereum blockchain",
        "animation_url": "https://test/",
        "name": "Chordus Arena Ancient Artefact #",
        "external_url": "https://www.chordusarena.com",
        "attributes": [
            ]
        }

    def __init__(self):
        self.meta = {
            "description": "Chordus Arena is a collection of unique, randomly generated collection of ancient artefacts on the Ethereum blockchain",
            "animation_url": "https://test/",
            "name": "Chordus Arena Ancient Artefact #",
            "attributes": [
                ]
            }
    
    def __del__(self):
        print("I'm being automatically destroyed. Goodbye!")

    def encode_to_json(self, id, type, element, rank, min_damage, max_damage, stats):

        self.meta["attributes"].append({"trait_type": "Type", "value": type})
        self.meta["attributes"].append({"trait_type": "Element", "value": element})
        self.meta["attributes"].append({"trait_type": "Rank", "value": rank})
        self.meta["attributes"].append({"trait_type": "MIN Damage", "value": int(min_damage)})
        self.meta["attributes"].append({"trait_type": "MAX Damage", "value": int(max_damage)})

        for stat in stats:
            self.meta["attributes"].append({"trait_type": stat[0], "value": int(stat[1])})
        
        self.meta["animation_url"] += self.generate_file_name(type, element, rank)

        self.meta["name"] += str(id)

        rawJSON = json.dumps(self.meta, indent=4)
        print(rawJSON)

    def generate_file_name(self, type, element, rank):
        type = re.sub('[\s+]', '', type).lower()
        return  type + '_' + element.lower() + '_' + rank.lower() + ".json"
