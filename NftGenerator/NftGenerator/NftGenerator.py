
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

print(gen.generate_legendary(10, 100))

#print(gen.select_random_element(25))

#I = range(1,20)

#array=[]

#for i in I:
#    array.append(i)

#print(array)

#np.random.shuffle(array)

#print(array)

#md.encode_to_json(1, "Neutral", "Base", "None")


