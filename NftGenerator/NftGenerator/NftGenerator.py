import numpy as np
from random import seed
from random import random
from random import randint
import json
import re

import constants
import metadata
import generator
import plotstats

TOTAL_NFTS = 5000

TEMP_PATH = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//tmp//"
TEMP_PATH_2 = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//tmp_2//"
FINAL_PATH = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//final//"
PREREVEAL_PATH = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//prereveal//"

def generate():
    base_nfts = int(TOTAL_NFTS * constants.BASE_NFTS)
    common_nfts = int(TOTAL_NFTS * constants.COMMON_NFTS)
    rare_nfts = int(TOTAL_NFTS * constants.RARE_NFTS)
    epic_nfts = int(TOTAL_NFTS * constants.EPIC_NFTS)
    legendary = int(TOTAL_NFTS * constants.LEGENDARY_NFTS)

    gen = generator.Generator()

    print(gen.generate_base_nfts(base_nfts, 1))
    minted_nfts = base_nfts
    print(gen.generate_common_nfts(common_nfts, minted_nfts + 1))
    minted_nfts += common_nfts
    print(gen.generate_rare_nfts(rare_nfts, minted_nfts + 1))
    minted_nfts += rare_nfts
    print(gen.generate_epic(epic_nfts, minted_nfts + 1))
    minted_nfts += epic_nfts
    print(gen.generate_legendary(legendary, minted_nfts + 1))
    minted_nfts += legendary

    gen.safe_to_files(TEMP_PATH)

    gen.shuffle_elements(gen.total_generated_nfts())

    gen.safe_to_files(TEMP_PATH_2)

    gen.shuffle_ids()

    gen.update_urls()

    gen.update_rarity()

    gen.safe_to_files(FINAL_PATH)

def generate_prereveal():
    I = range(0, TOTAL_NFTS)
    for i in I:
        md = metadata.Metadata()
        md.set_dummy_values(i + 1)
        file_name = PREREVEAL_PATH + str(i+1) + ".json"
        md.save(file_name)
        del md
    return

def plot():
    pl = plotstats.PlotStats()
    pl.plot()
    #pl.read_dir(FINAL_PATH)
    return

def test_image_urls(path):
    pl = plotstats.PlotStats()
    pl.read_dir(path)
    I = range(0, len(pl.metaArray))
    for i in I:
        print(i)
        pl.metaArray[i].verify_image_url()

def test():
    pl = plotstats.PlotStats()
    pl.read_dir(FINAL_PATH)
    return

def test_rarity():
    pl = plotstats.PlotStats()
    pl.read_dir(FINAL_PATH)
    pl.metaArray.sort(key=lambda x: x.rarity)
    I = range(0, len(pl.metaArray))
    for i in I:
        if(i == 0):
            if(pl.metaArray[i].rarity != 7):
                print("Error: first mast be 7")
                return
        if(i > 0):
            if(pl.metaArray[i-1].rarity + 1 != pl.metaArray[i].rarity):
                print("Error:", pl.metaArray[i-1].rarity, pl.metaArray[i].rarity)
                return
        print(pl.metaArray[i].rarity)

def main():
    generate_prereveal()
    #generate()
    #test_image_urls(PREREVEAL_PATH)
    #test_rarity()
    return
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()