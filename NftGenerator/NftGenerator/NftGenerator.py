
import numpy as np
from random import seed
from random import random
from random import randint
import json
import re

import metadata
import generator

 
#import re


##s = "1 2 3 4 5"
##print(re.sub('[\s+]', '', s))

##md = metadata.Metadata()

gen = generator.Generator()



print(gen.generate_epic(10, 1))
print(gen.generate_legendary(10, 11))

TEMP_PATH = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//tmp//"
TEMP_PATH_2 = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//tmp_2//"
FINAL_PATH = "D://OneDrive//BlockChain//workspace//nftgenerator//NftGenerator//NftGenerator//final//"

gen.safe_to_files(TEMP_PATH)

gen.shuffle_elements(gen.total_generated_nfts())

gen.safe_to_files(TEMP_PATH_2)

gen.shuffle_ids()

gen.safe_to_files(FINAL_PATH)



#md = metadata.Metadata()

#md.read("claw_dark_common.json")
#print(md.num_of_stats())
#print(md.get_min_damage())

#md.calculate_trp()

#print(gen.select_random_element(25))

#I = range(1,20)

#array=[]

#for i in I:
#    array.append(i)

#print(array)

#np.random.shuffle(array)

#print(array)

#md.encode_to_json(1, "Neutral", "Base", "None")


