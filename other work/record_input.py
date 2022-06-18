import csv
fields=['Name', 'Reporting_Manager', 'Project', 'Location', 'Gender', 'Start_Date', 'Recurring', 'End_Date', 'Start_Time', 'End_Time']
rows=[]

#rows = [['vishnu',"tarun","shift allowance service","jaipur","male","01-02-2022","y","01-03-2022","2100"],
#		['mohit',"tarun","Gym application","jaipur","male","01-02-2022","y","01-03-2022","2100"],
#		]

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

rows.append(list([name,reporting_manager,project,location,gender,start_date,recurring,end_date,start_time,end_time]))

filename= "logs.csv"
with open(filename, 'a') as csvfile:
	csvwriter = csv.writer(csvfile)
	#csvwriter.writerow(fields)
	csvwriter.writerows(rows)

print("\nShift Record Saved.")

#import email_automation