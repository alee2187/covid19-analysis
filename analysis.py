import csv
import datetime as dt
import matplotlib.pyplot as pl
from scripts import *
from data_analysis import *
import statistics as st


to_run = [1,1]

'''
0: INITIALIZE DATA
'''
if (to_run[0] == 1):
	c = Data("time_series_19-covid-Confirmed.csv")
	r = Data("time_series_19-covid-Recovered.csv")
	d = Data("time_series_19-covid-Deaths.csv")
	dtm,mtd = make_day_to_mdy(c.NUM_DATA)
	date_on_day = make_mdy_array(dtm,1,c.NUM_DATA)

'''
1: ANALYSIS SOUTH KOREA VS USA CASES/DELTAS
'''
if (to_run[1] == 0):
	
	fig, (ax_sk_cases,ax_us_cases) = pl.subplots(1,2)

	ax_sk_deltas = ax_sk_cases.twinx()
	ax_sk_cases.set_title("South Korea")
	ax_sk_deltas.bar([i for i in range(c.NUM_DATA)],[c.data_dict["Korea, South"]["Delta"][i] for i in range(c.NUM_DATA)],width=1,color="#bfefff")
	ax_sk_cases.plot(date_on_day,c.data_dict["Korea, South"]["Raw Data"],color="#00008B")
	
	
	ax_us_deltas = ax_us_cases.twinx()
	ax_us_cases.set_title("USA")
	ax_us_cases.plot(date_on_day,c.data_dict["US (Total)"]["Raw Data"],'b-')
	ax_us_deltas.bar([i for i in range(c.NUM_DATA)],[c.data_dict["US (Total)"]["Delta"][i] for i in range(c.NUM_DATA)],width=1,alpha=0.5)
	

	# ax2 = ax1.twinx()
	# ax.plot(x, y1, 'g-')
	# ax2.plot(x, y2, 'b-')

	# ax1.set_xlabel('X data')
	# ax1.set_ylabel('Y1 data', color='g')
	# ax2.set_ylabel('Y2 data', color='b')


# print(d.data_dict["US (Total)"]["Delta"])
# print(c.data_dict["US (Total)"]["Ratios"])
# print(c.data_dict["US (Total)"]["Doubling Times"])
# oldlst = c.data_dict["US (Total)"]["Doubling Times"]
# lst = []
# for i in oldlst[-20:]:
# 	if (i >= 0):
# 		lst.append(i)
# avg = sum(lst)/len(lst)
# std = st.stdev(lst)
# print(avg)
# print(avg-2*std)
# print(avg+1*std)

# print()
# print()
# dum=0
# deathrate=[]
# for i in range(c.NUM_DATA):
# 	try:
# 		deathnum = 1/d.data_dict["US (Total)"]["Raw Data"][i]
# 		deathnum = 100*d.data_dict["US (Total)"]["Raw Data"][i] / c.data_dict["US (Total)"]["Raw Data"][i]
# 		deathrate.append(deathnum)
# 	except:
# 		dum += 1

avgcurve = c.data_dict["Italy"]["Delta"]
avgcurvenew = avgcurve
for i in range(4,c.NUM_DATA):
	avgcurvenew[i] = (avgcurve[i]+avgcurve[i-1]+avgcurve[i-2]+avgcurve[i-3]+avgcurve[i-4])/5

# pl.plot(avgcurvenew)
doubles = []
for i in range(1,len(avgcurvenew)):
	try:
		doubles.append(1/math.log(avgcurvenew[i]/avgcurvenew[i-1],2))
	except:
		doubles.append(-1)
print(doubles)
pl.plot(avgcurvenew)
# pl.show()

lst = []
for i in doubles[-20:]:
	if (i > 0):
		lst.append(i)
avg = sum(lst)/len(lst)
std = st.stdev(lst)
print(avg)
print(std)
print(avg-std)
print(avg+std)

print()
print()
print(c.data_dict["US (Total)"]["Delta"])