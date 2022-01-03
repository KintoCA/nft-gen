import constants
import metadata
import numpy as np
from random import seed
from random import random
from random import randint


class Generator(object):

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
			elements.append(constants.ELEMENT[element_ids[i]])
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
			md.encode_to_json(i + start_id, types[i], elements[i], "Base", min_damage[i], max_damage[i], stats)
			del md
		return

	def add_parameters_to_stats(self, stats, stats_range):
		parameters = np.random.randint(stats_range[0], stats_range[1], len(stats))
		I = range(0, len(stats))
		parameterized_stats = []
		for i in I:
			parameterized_stats.append([stats[i], parameters[i]])
		return parameterized_stats

	def generate_nfts_gen(self, min_damage_range, max_damage_range, stats_range, stats_num, nft_number, start_id):
		min_damage = np.random.randint(min_damage_range[0], min_damage_range[1], nft_number)
		max_damage = np.random.randint(max_damage_range[0], max_damage_range[1], nft_number)
		elements = self.select_random_element(nft_number)
		types = self.select_random_type(nft_number)
		I = range(0, nft_number)
		all_stats = self.select_random_stats(stats_num, nft_number)
		for i in I:
			parameterized_stats = self.add_parameters_to_stats(all_stats[i], stats_range)
			md = metadata.Metadata()
			md.encode_to_json(i + start_id, types[i], elements[i], "Common", min_damage[i], max_damage[i], parameterized_stats)
			del md

	def generate_common_nfts(self, nft_number, start_id):
		MIN_DAMAGE = (185, 355)
		MAX_DAMAGE = (355, 525)
		STATS_RANGE	= (20, 60)
		STATS_NUM    = 1
		self.generate_nfts_gen(MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)


	def generate_rare_nfts(self, nft_number, start_id):
		MIN_DAMAGE = (250, 420)
		MAX_DAMAGE = (420, 590)
		STATS_RANGE	= (26, 66)
		STATS_NUM      = 2
		self.generate_nfts_gen(MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)

	def generate_epic(self, nft_number, start_id):
		MIN_DAMAGE = (315, 485)
		MAX_DAMAGE = (485, 655)
		STATS_RANGE	= (32, 69)
		STATS_NUM      = 3
		self.generate_nfts_gen(MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)

	def generate_legendary(self, nft_number, start_id):
		MIN_DAMAGE = (380, 550)
		MAX_DAMAGE = (550, 720)
		STATS_RANGE	= (38, 75)
		STATS_NUM = 4
		self.generate_nfts_gen(MIN_DAMAGE, MAX_DAMAGE, STATS_RANGE, STATS_NUM, nft_number, start_id)
