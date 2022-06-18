import datetime
lpa=100000
cutoff_time=22 # "22:00" || 10 PM

# PART -1 Validation for 9 hr duty.
h1,m1=map(int,input("start_time: ").split(":"))
h2,m2=map(int,input("end_start: ").split(":"))

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
		incr= ctc/10	# 10%
		ctc+=incr
	elif diff>=3 and diff<5:
		incr= ctc/4		# 25%
		ctc+=incr
	elif diff>=5:
		incr= ctc/2		# 50%
		ctc+=incr
	else:
		print("\nNot Eligible for Allowance.")

	print("Shift Allowance Increament: ", ctc)

else:
	print("Time Limit Exceeding.")
