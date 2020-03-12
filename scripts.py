import csv
import datetime as dt
import matplotlib.pyplot as pl

class Data:
	'''
	Data: class for each individual data set (confirmed cases, deaths, recovered)
	'''
	def __init__(self,filename):
		with open(filename) as csvfile:
			self.read_in_data = csv.DictReader(csvfile,delimiter=",")
		


confirmed_cases = Data("ts.csv")