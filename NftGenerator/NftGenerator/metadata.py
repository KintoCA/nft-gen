import json

class Metadata():

    meta  = {
        "description": "Chordus Arena Artefact",
        "external_url": "https://test/",
        "image": "https://test/",
        "name": "",
        "attributes": [
            {"trait_type": "Type", "value": ""},
            {"trait_type": "Element", "value": ""},
            {"trait_type": "Rank", "value": ""},
            {"trait_type": "MIN Damage", "value": 0},
            {"trait_type": "MAX Damage", "value": 0}
            ]
        }

    def encode_to_json(self, id, element, rank, stats):
        print(self.meta["attributes"][0]["trait_type"])
        self.meta["attributes"][0]["trait_type"] = element
        self.meta["attributes"][1]["trait_type"] = rank
        self.meta["external_url"] += (str(id) + ".json")
        self.meta["image"] += (str(id) + ".mp4")
#        print(self.meta["attributes"])
        rawJSON = json.dumps(self.meta, indent=4)
        print(rawJSON)


