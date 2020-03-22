import datetime as dt

def make_day_to_mdy(day):
		day_to_mdy = {}
		for i in range(0,day+1):
			try:
				day_to_mdy[i] = dt.date(2020,1,21+i).strftime("%m/%d/%Y")
			except:
				try:
					day_to_mdy[i] = dt.date(2020,2,i-10).strftime("%m/%d/%Y")
				except:
					try: 
						day_to_mdy[i] = dt.date(2020,3,i-39).strftime("%m/%d/%Y")
					except:
						try:
							day_to_mdy[i] = dt.date(2020,4,i-70).strftime("%m/%d/%Y")
						except:
							try: 
								day_to_mdy[i] = dt.date(2020,5,i-100).strftime("%m/%d/%Y")
							except:
								try:
									day_to_mdy[i] = dt.date(2020,6,i-131).strftime("%m/%d/%Y")
								except:
									break
		mdy_to_day = dict(map(reversed,day_to_mdy.items()))
		return day_to_mdy, mdy_to_day

def make_mdy_array(dtm,date_start,NUM_DATA):
	date_on_day = [dtm[date_start-1][0:5]]
	for i in range(date_start,NUM_DATA + 1):
		to_add_to_date = " "*i
		if (i%7 == 0):
			to_add_to_date = str(dtm[i][0:5])
		date_on_day.append(to_add_to_date)
	return date_on_day

# dtm,mtd = make_day_to_mdy(200)
# print(dtm)