import constants
import metadata
import os
import numpy as np
from random import seed
from random import random
from random import randint


class Generator(object):

	metaArray = []

	def select_random_stats(self, max_number_of_stats, nft_number):
		all_stats = []
		NFT_RANGE = range(0, nft_number)
		for i in NFT_RANGE:
			all_stats.append(self.not_duplicated_stats(max_number_of_stats))
		return all_stats

	def not_duplicated_stats(self, max_number_of_stats):
		ready_to_go = True
		while ready_to_go:
			stat_ids = np.random.randint(0, len(constants.STATS), max_number_of_stats)
			#print(stat_ids)
			ready_to_go = self.find_duplicates(stat_ids)	
		stats = []
		for i in stat_ids:
			stats.append(constants.STATS[i])
		return stats

	def select_random_element(self, nft_number):
		element_ids = np.random.randint(0, len(constants.ELEMENT), nft_number)
		print(element_ids)
		elements = []
		I = range(0, len(element_ids))
		for i in I:
			elements.append(constants.ELEMENT[element_ids[i]][0])
		return elements

	def select_random_type(self, nft_number):
		type_ids = np.random.randint(0, len(constants.TYPE), nft_number)
		print(type_ids)
		types = []
		I = range(0, len(type_ids))
		for i in I:
			types.append(constants.TYPE[type_ids[i]])
		return types

	def select_random_rank(self, nft_number):
		rank_ids = np.random.randint(0, len(constants.RANK), nft_number)
		print(rank_ids)
		ranks = []
		I = range(0, len(rank_ids))
		for i in I:
			ranks.append(constants.RANK[rank_ids[i]])
		return ranks


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

	def add_parameters_to_stats(self, stats, stats_range):
		parameters = np.random.randint(stats_range[0], stats_range[1], len(stats))
		I = range(0, len(stats))
		parameterized_stats = []
		for i in I:
			parameterized_stats.append([stats[i], parameters[i]])
		return parameterized_stats

	def generate_nfts_gen(self, rank, min_damage_range, max_damage_range, stats_range, stats_num, nft_number, start_id):
		min_damage = np.random.randint(min_damage_range[0], min_damage_range[1], nft_number)
		max_damage = np.random.randint(max_damage_range[0], max_damage_range[1], nft_number)
		elements = self.select_random_element(nft_number)
		types = self.select_random_type(nft_number)
		I = range(0, nft_number)
		all_stats = self.select_random_stats(stats_num, nft_number)
		for i in I:
			parameterized_stats = self.add_parameters_to_stats(all_stats[i], stats_range)
			md = metadata.Metadata()
			md.set_all_values(i + start_id, types[i], elements[i], rank, min_damage[i], max_damage[i], parameterized_stats)
			self.metaArray.append(md)
			del md

	def generate_base_nfts(self, nft_number, start_id):
		MIN_DAMAGE	= (120, 290)
		MAX_DAMAGE	= (290, 460)
		min_damage = np.random.randint(MIN_DAMAGE[0], MIN_DAMAGE[1], nft_number)
		max_damage = np.random.randint(MAX_DAMAGE[0], MAX_DAMAGE[1], nft_number)
		elements = self.select_random_element(nft_number)
		types = self.select_random_type(nft_number)
		I = range(0, nft_number)
		stats = []
		for i in I:
			md = metadata.Metadata()
			md.set_all_values(i + start_id, types[i], elements[i], "Base", min_damage[i], max_damage[i], stats)
			self.metaArray.append(md)
			del md
		return
	
	def generate_common_nfts(self, nft_number, start_id):
		MIN_DAMAGE = (185, 355)
		MAX_DAMAGE = (355, 525)
		STATS_RANGE	= (20, 60)
		STATS_NUM    = 1
		self.generate_nfts_gen("Common", MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)


	def generate_rare_nfts(self, nft_number, start_id):
		MIN_DAMAGE = (250, 420)
		MAX_DAMAGE = (420, 590)
		STATS_RANGE	= (26, 66)
		STATS_NUM      = 2
		self.generate_nfts_gen("Rare", MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)

	def generate_epic(self, nft_number, start_id):
		MIN_DAMAGE = (315, 485)
		MAX_DAMAGE = (485, 655)
		STATS_RANGE	= (32, 69)
		STATS_NUM      = 3
		self.generate_nfts_gen("Epic", MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)

	def generate_legendary(self, nft_number, start_id):
		MIN_DAMAGE = (380, 550)
		MAX_DAMAGE = (550, 720)
		STATS_RANGE	= (38, 75)
		STATS_NUM = 4
		self.generate_nfts_gen("Legendary", MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)

	def safe_to_files(self, dir_name):
		for md in self.metaArray:
			path = os.path.join(dir_name, md.get_nft_file_name())
			md.save(path)

	def total_generated_nfts(self):
		return len(self.metaArray)

	def shuffle_elements(self, total_nft):
		arrayElementsId = []
		total_neutral = int(total_nft * constants.ELEMENT[0][1])
		I = range(0, total_neutral)
		for i in I:
			arrayElementsId.append(0)
		print(arrayElementsId)
		print(len(arrayElementsId))

		total_poison = int(total_nft * constants.ELEMENT[1][1])
		I = range(0, total_poison)
		for i in I:
			arrayElementsId.append(1)
		print(arrayElementsId)
		print(len(arrayElementsId))

		total_fire = int(total_nft * constants.ELEMENT[2][1])
		I = range(0, total_fire)
		for i in I:
			arrayElementsId.append(2)
		print(arrayElementsId)
		print(len(arrayElementsId))

		total_frost = int(total_nft * constants.ELEMENT[3][1])
		I = range(0, total_frost)
		for i in I:
			arrayElementsId.append(3)
		print(arrayElementsId)
		print(len(arrayElementsId))

		total_light = int(total_nft * constants.ELEMENT[4][1])
		I = range(0, total_light)
		for i in I:
			arrayElementsId.append(4)
		print(arrayElementsId)
		print(len(arrayElementsId))

		rest = int(total_neutral + total_poison + total_fire + total_frost + total_light)
		total_dark = total_nft - rest 
		I = range(0, total_dark)
		for i in I:
			arrayElementsId.append(5)
		print(arrayElementsId)
		print(len(arrayElementsId))

		np.random.shuffle(arrayElementsId)
		I = range(0, len(arrayElementsId))
		for i in I:
			self.metaArray[i].set_element(constants.ELEMENT[arrayElementsId[i]][0])
			print(constants.ELEMENT[arrayElementsId[i]][0])

	def update_urls(self):
		I = range(0, len(self.metaArray))
		for i in I:
			self.metaArray[i].update_image_url()

	def shuffle_ids(self):
		I = range(1, len(self.metaArray) + 1)
		arrayIds = []
		for i in I:
			arrayIds.append(i)
		np.random.shuffle(arrayIds)
		I = range(0, len(self.metaArray))
		for i in I:
			self.metaArray[i].set_id(arrayIds[i])
		print(arrayIds)

	def update_rarity(self):
		self.metaArray.sort(key=lambda x: x.rarity, reverse=True)
		I = range(0, len(self.metaArray))
		for i in I:
			print(self.metaArray[i].id, self.metaArray[i].rarity, i+7)
			self.metaArray[i].set_rarity(i+7)
