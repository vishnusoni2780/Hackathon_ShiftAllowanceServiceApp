"""
manager allocating incoming time to employees,
e.g- 
-> star_time=5 PM, end_time=2 AM (according to 9 hrs work/day)
	so whatevere extra hrs he is in circuit of 9hrs doing after 10 PM will include as extra hrs and will be eligible for allowance

	5 PM - 10 PM --> 5HRS COMPLETE
	NEXT 4 HR IS IN ALLOWANCE AS 25%

-> start=3 PM, end=12 AM
	3 PM - 10 PM --> 7 HRS COMPLETE
	NEXT 2 HR IS IN ALLOWANCE AS 10%

-> start=6 PM, end=3 AM
	6 PM - 10 PM --> 4 HRS COMPLETE
	NEXT 5 HR IS IN ALLOWANCE AS 50%


-> No constraint to end_time parameter it is only for 9hrs validation.

-------------------------------------------------
*** unit test for record_input_db:
	(i)   18:00 , 04:00 => error
	(ii)  18:00 , 03:00 => end_limit case
	(iii) 19:00 , 03:00 => 50% allowance case
	(iv) 18:00 , 01:15 => 25%
	(v)  18:00 , 12:30 => 10%
"""
def timings(start_time,end_time):
	import datetime,time
	lpa=100000
	cutoff_time=22 # "22:00" || 10 PM

	# PART -1 Validation for 9 hr duty.
	h1,m1=map(int,start_time.split(":"))
	h2,m2=map(int,end_time.split(":"))

	time_1 = datetime.timedelta(hours= h1, minutes=m1)
	time_2 = datetime.timedelta(hours= h2, minutes=m1)
	time_interval = time_2 - time_1

	#print("Time Duration: ",time_interval)	#init OP will have -day extra.

	try:
		h,m,s=map(int,str(time_interval).split(":"))
	except:
		day,main= map(str,str(time_interval).split(","))
		h,m,s=map(int,str(main).split(":"))

	# PART -1 Ends Here.

	if h<=9:
		t2= datetime.timedelta(hours=cutoff_time,minutes=00) #for 10PM deadline
		WorkDoneBefore_10PM = t2-time_1
	#	print("WorkDoneBefore_10PM: ",WorkDoneBefore_10PM)
		try:
			WorkDone_HR, WorkDone_MIN, WorkDone_S=map(int,str(WorkDoneBefore_10PM).split(":"))
		except:
			day1,main1= map(str,str(WorkDoneBefore_10PM).split(","))
			WorkDone_HR, WorkDone_MIN, WorkDone_S=map(int,str(main1).split(":"))

		RemainingWork= h- WorkDone_HR
	#	print("h,WorkDone_HR:", h, WorkDone_HR)
	#	print("Remaining Work: ",RemainingWork)
		diff=RemainingWork
		ctc= 6*lpa

		if diff>=2 and diff<3:
			incr=  10 # %
			#ctc+=incr
			return incr

		elif diff>=3 and diff<5:
			incr=  25 # %
			#ctc+=incr
			return incr

		elif diff>=5:
			incr= 50 # %
			#ctc+=incr
			return incr

		else:
			print("\nNot Eligible for Allowance.")
			time.sleep(2)

#		print("Shift Allowance Increament: ", ctc)
	else:
		print("\nTime Limit Exceeding.")
		time.sleep(2)