import csv
import time,os

fields=['Name', 'Reporting_Manager', 'Project', 'Location', 'Gender', 'Start_Date', 'Recurring', 'End_Date', 'Start_Time', 'End_Time']

print("Input the required data...\n")
name=input("Enter Name of Employee: ")
reporting_manager=input("Enter Reporting Manager Name: ")
project=input("Project Name: ")
location=input("Office Location: ")
gender=input("Gender: ")
start_date=input("Start Date: ")
recurring=input("Recurring [y/n]: ")
end_date=input("End Date: ")
start_time=input("Start Time: ")
end_time=input("End Time: ")

print("\nAppending shift record to logs...")
time.sleep(2)

rows=[name,reporting_manager,project,location,gender,start_date,recurring,end_date,start_time,end_time]
filename= "logs.csv"

with open(filename, 'a',newline='',encoding='utf-8') as csvfile:
	csvwriter = csv.writer(csvfile)

	if os.stat("logs.csv").st_size == 0:
		print("\nAdding Field...")
		time.sleep(2)
		csvwriter.writerow(fields)
	
	print("\nAdding Rows...")
	time.sleep(2)
	csvwriter.writerow(rows)
print("\nRecord added.")

print("\nData Cleaning intialization...")


#import email_automation

#rows = [['vishnu',"tarun","shift allowance service","jaipur","male","01-02-2022","y","01-03-2022","2100"],
#		['mohit',"tarun","Gym application","jaipur","male","01-02-2022","y","01-03-2022","2100"],
#		]
