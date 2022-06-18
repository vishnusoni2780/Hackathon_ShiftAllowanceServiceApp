def trig():
	import datetime,time
	curr_date= datetime.datetime.now()

	info=curr_date
	Year=curr_date.year
	Month=curr_date.month
	Day=curr_date.day

	"""
	print("info: ",curr_date)
	print("Year: ",curr_date.year)
	print("Month: ",curr_date.month)
	print("Day: ",curr_date.day)
	"""
	if Day==15 or Day==22:
		import email_automation as e_a
		e_a.alert_notif(Day)
	else:
		print("\nNot Today !")
		time.sleep(2)

	return True

def update():
	#updation starts from here.
	import time
	upd=input("\nWant to update the records [y/n]: ")

	if upd=='y':
		import update_xl
		update_xl.up_xl()

	else:
		print("\nNothing Updated => Good to Go.")
		time.sleep(2)

	return True
