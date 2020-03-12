import csv
import datetime as dt
import matplotlib.pyplot as pl
from scripts import *



class Data:
	'''
	Data: class for each individual data set (confirmed cases, deaths, recovered)
	'''
	def __init__(self,filename):
		with open(filename) as csvfile:
			self.readin = csv.reader(csvfile,delimiter=",")
			self.readin_dictlist = []
			for row in self.readin:
				self.readin_dictlist.append(row)
		self.data_dict = {}
		self.NUM_DATA = len(self.readin_dictlist[0])-4
		self.NUM_PLACES = len(self.readin_dictlist)-1
		dtm, mtd = make_day_to_mdy(self.NUM_DATA)

		split_countries_list = set()

		for place_number in range(1,self.NUM_PLACES+1):

			this_place = {}
			this_place["Country"] = self.readin_dictlist[place_number][1]
			this_place["Region"] = self.readin_dictlist[place_number][0]

			if (len(self.readin_dictlist[place_number][0]) == 0):
				location_tag = self.readin_dictlist[place_number][1]
				this_place["Location"] = this_place["Country"]
			else:
				location_tag = self.readin_dictlist[place_number][0] + " :: " + self.readin_dictlist[place_number][1]
				this_place["Location"] = location_tag
				this_place["Region"] = self.readin_dictlist[place_number][0]
				split_countries_list.add(this_place["Country"])

			for i in range(4,self.NUM_DATA+4):
				this_place[dtm[i-3]] = self.readin_dictlist[place_number][i]
			self.data_dict[location_tag] = this_place

		for countries in split_countries_list:
			this_place = {}
			this_place["Country"] = countries
			this_place["Location"] = countries
			regions_in_country = set()
			for places in self.data_dict:
				if (self.data_dict[places]["Country"] == countries):
					regions_in_country.add(self.data_dict[places]["Region"])

			for i in range(1,self.NUM_DATA+1):
				dummy_var_1 = 0
				for regions in regions_in_country:
					dummy_var_1 += int(self.data_dict[regions + " :: " + countries][dtm[i]])
				this_place[dtm[i]] = dummy_var_1
			self.data_dict[countries + " (Total)"] = this_place




c = Data("time_series_19-covid-Confirmed.csv")

# for row in range(c.NUM_PLACES):
# 	print(c.readin_dictlist[row])
# 	print()

for row in c.data_dict:
	print(row)
	print(c.data_dict[row])
