import datetime as dt

def make_day_to_mdy(day):
		day_to_mdy = {}
		for i in range(1,day+1):
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

dtm,mtd = make_day_to_mdy(200)
print(dtm)