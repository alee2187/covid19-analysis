import csv
import datetime as dt
import matplotlib.pyplot as pl
import math
from scripts import *



class Data:
	'''
	Data: class for each individual data set (confirmed cases, deaths, recovered)
	'''
	def __init__(self,filename):

		'''
		INITIALIZING DICTIONARY
		'''

		# Initial Data In
		####
		with open(filename) as csvfile:
			self.readin = csv.reader(csvfile,delimiter=",")
			self.readin_dictlist = []
			for row in self.readin:
				self.readin_dictlist.append(row)
		self.data_dict = {}
		self.NUM_DATA = len(self.readin_dictlist[0])-4
		self.NUM_PLACES = len(self.readin_dictlist)-1
		self.dtm, self.mtd = make_day_to_mdy(self.NUM_DATA)
		###

		# Making the initial dictionary
		###
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

			temp_data_array_1 = [0]
			for i in range(4,self.NUM_DATA+4):
				temp_data_array_1.append(int(self.readin_dictlist[place_number][i]))
			this_place["Raw Data"] = temp_data_array_1
			self.data_dict[location_tag] = this_place
		#####

		# Adding World count to dictionary
		###
		this_place = {}
		this_place["Country"] = "World"
		this_place["Location"] = "World"
		temp_data_array_3 = [0]*(self.NUM_DATA+1)
		for places in self.data_dict:
			for i in range(1,self.NUM_DATA+1):
				temp_data_array_3[i] += int(self.data_dict[places]["Raw Data"][i])
		this_place["Raw Data"] = temp_data_array_3
		self.data_dict["World"] = this_place
		#####

		# Adding totals to dictionary
		###
		for countries in split_countries_list:
			this_place = {}
			this_place["Country"] = countries
			this_place["Location"] = countries
			regions_in_country = set()
			for places in self.data_dict:
				if (self.data_dict[places]["Country"] == countries):
					regions_in_country.add(self.data_dict[places]["Region"])
			
			temp_data_array_2 = [0]*(self.NUM_DATA+1)
			for regions in regions_in_country:
				for i in range(1,self.NUM_DATA+1):
					temp_data_array_2[i] += int(self.data_dict[regions + " :: " + countries]["Raw Data"][i])
			this_place["Raw Data"] = temp_data_array_2
			self.data_dict[countries + " (Total)"] = this_place
		#####

		'''
		ANALYSIS
		'''
		# Adding new cases per day array for each subdictionary (region)
		for locations in self.data_dict:
			temp_data_array_4 = [0]
			temp_data_array_5 = [1]
			temp_data_array_6 = [0]
			dummy_var_1 = 0
			dummy_var_2 = 1
			dummy_var_3 = 1
			for days in range(1,self.NUM_DATA+1):
				dummy_var_1 = self.data_dict[locations]["Raw Data"][days] - self.data_dict[locations]["Raw Data"][days-1]
				temp_data_array_4.append(dummy_var_1)
			self.data_dict[locations]["Delta"] = temp_data_array_4
			for days in range(1,self.NUM_DATA+1):
				if (self.data_dict[locations]["Delta"][days-1] != 0):
					dummy_var_2 = self.data_dict[locations]["Delta"][days] / self.data_dict[locations]["Delta"][days-1]
				else:
					dummy_var_2 = 1 
				try:
					dummy_var_3 = 1/math.log(dummy_var_2,2)
				except: 
					dummy_var_3 = 0
				
				temp_data_array_5.append(dummy_var_2)
				temp_data_array_6.append(dummy_var_3)
			
			self.data_dict[locations]["Ratios"] = temp_data_array_5
			self.data_dict[locations]["Doubling Times"] = temp_data_array_6

	def plot_data(self,location_tag,date_start,plot_title,plot_color,show=False,scale="log",data_type="Raw Data"):
		if (show == True):
			fig = pl.figure()
			ax = pl.axes()
			pl.title(plot_title)

		if (show == True):
			ax.set_yscale(scale)
			ax.plot(self.date_on_day,self.cases_on_day,color=plot_color)
			ax.plot(self.date_on_day,self.cases_on_day,color=plot_color,marker='.',markersize='10')
			ax.yaxis.grid(color='gray',alpha=10,linewidth='1')
			pl.show()
		return

###############################

# def plot_data_cd(location_tag,date_start,c,d,show=False,scale="log",cdr = "Confirmed Cases and Deaths in ",data_type="Raw Data"):
# 	fig = pl.figure()
# 	ax = pl.axes()
# 	data_type_blurb = cdr
# 	pl.title(data_type_blurb + location_tag)

# 	ax.set_yscale(scale)
# 	ax.plot(c.date_on_day,c.cases_on_day,color="blue")
# 	ax.plot(d.date_on_day,d.cases_on_day,color="red")
# 	ax.plot(c.date_on_day,c.cases_on_day,color='blue',marker='.',markersize=10)
# 	ax.plot(d.date_on_day,d.cases_on_day,color='red',marker='.',markersize=10)

# 	ax.yaxis.grid(color='gray',alpha=10,linewidth='1')
# 	if(show==True):
# 		pl.show()
# 	return
# c = Data("time_series_19-covid-Confirmed.csv")
# r = Data("time_series_19-covid-Recovered.csv")
# d = Data("time_series_19-covid-Deaths.csv")


# # plot multiple locations

# location_tags = ["Korea, South"]
# # location_tags = []

# # for locations in location_tags:
# # 	the_scale="log"
# # 	the_data_type="Raw Data"
# # 	c.plot_data(locations,1,cdr='c',show=False,scale=the_scale,data_type=the_data_type)
# # 	d.plot_data(locations,1,cdr='d',show=False,scale=the_scale,data_type=the_data_type)
# # 	plot_data_cd(locations,1,c,d,show=True,scale=the_scale,data_type=the_data_type)

# # for row in range(c.NUM_PLACES):
# # 	print(c.readin_dictlist[row])
# # 	print()

# # for row in c.data_dict:
# # 	print(row)
# # 	print(c.data_dict[row])

# # outputs tab-separated data for use in desmos
# # i = -1-1
# # location_tag = "US (Total)"
# # for days in c.data_dict[location_tag]:
# # 	if (i > 0):
# # 		print(i,end="\t")
# # 		print(c.data_dict[location_tag][days],end = "\n")
# # 	i+=1

# print(c.data_dict["US (Total)"]["Raw Data"])
# print(c.data_dict["Korea, South"]["Raw Data"])
