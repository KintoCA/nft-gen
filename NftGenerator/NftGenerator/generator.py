import numpy as np
from random import seed
from random import random
from random import randint



class Generator(object):

	COMMON_STATS_NUM    = 1
	RARE_STATS_NUM      = 2
	EPIC_STATS_NUM      = 3
	LEGENDARY_STATS_NUM = 4

	STATS = ["Strength", "HP", "Evasion", "Accuracy", "Resistance", "Reflex"]
	ELEMENT = ["Neutral", "Poison", "Fire", "Frost", "Light", "Dark"]
	TYPE = ["Axe", "Claw", "Great Sword", "Hammer", "Shield", "Sicle", "Sword"]

	def select_random_stats(self, max_number_of_stats, nft_number):
		all_stats = []
		NFT_RANGE = range(0, nft_number)
		for i in NFT_RANGE:
			all_stats.append(self.not_duplicated_stats(max_number_of_stats))
		return all_stats

	def not_duplicated_stats(self, max_number_of_stats):
		ready_to_go = True
		while ready_to_go:
			stat_ids = np.random.randint(0, len(self.STATS), max_number_of_stats)
			#print(stat_ids)
			ready_to_go = self.find_duplicates(stat_ids)	
		stats = []
		for i in stat_ids:
			stats.append(self.STATS[i])
		return stats

	def select_random_element(self, nft_number):
		element_ids = np.random.randint(0, len(self.ELEMENT), nft_number)
		print(element_ids)
		elements = []
		I = range(0, len(element_ids))
		for i in I:
			elements.append(self.ELEMENT[element_ids[i]])
		return elements

	def select_random_type(self, nft_number):
		type_ids = np.random.randint(0, len(self.TYPE), nft_number)
		print(type_ids)
		types = []
		I = range(0, len(type_ids))
		for i in I:
			types.append(self.TYPE[element_ids[i]])
		return types

	def find_duplicates(self, list):
		I = range(0, len(list))
		for i  in I:
			#print("--------------------")
			J = range(i+1, len(list))
			for j in J:
				#print(str(i) + " " + str(j))
				#print(str(list[i]) + " " + str(list[j]))
				if list[i] == list[j]:
					#print("********** duplicates found: " + str(list[i]) + " " + str(list[j]))
					return True
		return False

	def find_item(self, list, item):
		count = 0 
		while count < len(list):
			if item == list[count]:
				return True
			print(list[count])
			count += 1
		return False

	def generate_base(self, nft_number):
		MIN_DAMAGE	= (120, 290)
		MAX_DAMAGE	= (290, 460)
		self.select_random_element(self, nft_number)
		min_damage = np.random.randint(120, 290, nft_number)
		max_damage = np.random.randint(290, 460, nft_number)
		nfts = []
		I = range(0, nft_number)
		#for i in I:

		return

	def generate_common(self):
		MIN_DAMAGE = (185, 355)
		MAX_DAMAGE = (355, 525)
		STRENGHT	= (20, 60)
		HP			= (20, 60)
		EVASION		= (20, 60)
		ACCURACY	= (20, 60)
		RESISTANCE  = (20, 60)
		REFLEX		= (20, 60)

		return

	def generate_rare(self):
		MIN_DAMAGE = (250, 420)
		MAX_DAMAGE = (420, 590)
		STRENGHT	= (26, 66)
		HP			= (26, 66)
		EVASION		= (26, 66)
		ACCURACY	= (26, 66)
		RESISTANCE  = (26, 66)
		REFLEX		= (26, 66)
		return

	def generate_epic(self):
		MIN_DAMAGE = (315, 485)
		MAX_DAMAGE = (485, 655)
		STRENGHT	= (32, 69)
		HP			= (32, 69)
		EVASION		= (32, 69)
		ACCURACY	= (32, 69)
		RESISTANCE  = (32, 69)
		REFLEX		= (32, 69)

		return

	def generate_legendary(self):
		MIN_DAMAGE = (380, 550)
		MAX_DAMAGE = (550, 720)
		STRENGHT	= (38, 75)
		HP			= (38, 75)
		EVASION		= (38, 75)
		ACCURACY	= (38, 75)
		RESISTANCE  = (38, 75)
		REFLEX		= (38, 75)

		return
