def record():
	import sqlite3
	import csv
	import time,os

	print("\nConnecting to Database...")
	time.sleep(2)

	conn=sqlite3.connect("logs.sqlite")
	cur=conn.cursor()

	if os.stat("logs.sqlite").st_size == 0:
		print("\nCreating Table...")
		time.sleep(2)
		cur.execute("CREATE TABLE DATA(Name TEXT, Reporting_Manager TEXT, Project TEXT, Location TEXT, Gender TEXT, Start_Date VARCHAR, Recurring TEXT, End_Date VARCHAR, Start_Time VARCHAR, End_Time VARCHAR, Allowance INT);")
		print("Table created.")

	print("\nInput the required data...")
	name=input("\nEnter Name of Employee: ")
	reporting_manager=input("Enter Reporting Manager Name: ")
	project=input("Project Name: ")
	location=input("Office Location: ")
	gender=input("Gender: ")
	start_date=input("Start Date: ")
	recurring=input("Recurring [y/n]: ")
	end_date=input("End Date: ")
	start_time=input("Start Time: ")
	end_time=input("End Time: ")

	import shift_allowance as sa
	incr=sa.timings(start_time,end_time)

	if type(incr)==type(1):
		print("\nAppending shift record to logs...")
		time.sleep(2)

		cur.execute("INSERT INTO DATA (Name, Reporting_Manager, Project, Location, Gender, Start_Date, Recurring, End_Date, Start_Time, End_Time, Allowance) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(name,reporting_manager,project,location,gender,start_date,recurring,end_date,start_time,end_time,incr))
		cur.execute("commit;")
		conn.close()
		print("\nRecord added.")
		time.sleep(2)

		import email_automation as e_a
		e_a.email_for_new()

		return True

	else:
		return True