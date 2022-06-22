# Hackathon_ShiftAllowanceServiceApp
# Shift Allowance Service App - Console based using Python.

# PPT presentation for this project
https://docs.google.com/presentation/d/1UqRwlUifnAjKL4NpmlsCbZ39D5LqnuQ3/edit?usp=drivesdk&ouid=117655755480663494982&rtpof=true&sd=true

# Packages
- first of all use: 'pip install -r requirements.txt'
- For a Virtual Testing env in python:
	- pip install virtualenv		# lib require
	- py -m venv testing			# virtual env named 'testing'
	- testing\Scripts\activate 		# jump to normal env -> virtual env
	- testing\Scripts\deactivate 	# to come back to normal env
- And then these are the main python scripts which are part of project.

- ShiftAllowanceServiceApp.py [Main .py file]
- record_input_db.py
- shift_allowance.py
- date_trigger.py
- export_xl.py
- update_xl.py
- email_automation.py

# Data Storage
- logs.sqlite
- output.xlsx

# ShiftAllowanceServiceApp.py

- As per the problem statement the requirements are listed as per choice, which keeps on loop untill user doesn't want to exit.
- Any other input will alert as Invalid Choice.

# Choice:1 => Enter New Shift Record
	
- In this, a new record will be added at the end. First the 'record_input_db.py' package will be imported and calling it's function named as 'record()'.
- This function contains several functionallity sunch as:
	- Connecting to DataBase (SQLite DB Browser)
	- Creating 'logs.sqlite' file to store logs.
	- Creating Table in DB named as 'DATA'
	- Demanding the Input of data from user:
		- Name
		- Reporting_Manager
		- Project
		- Location
		- Gender
		- Start_Date
		- Recurring
		- End_Date
		- Start_Time
		- End_Time
	- Calculating Shift Allwance based on 'start_time' & 'end_time' (24 hr format)
		- PART 1 Validation for 9 hr of duty
		- if time is greater than 9 hrs, "Time Limit Exceeding" Alert will be display otherwise move on to further.
		- PART 2 Calculating actual hrs worked after 22:00 hrs (10:00 PM)
		- After this the hr will be checked on provided 3 conditions of calculating shift allowance.
		- If not meets any criteria of getting allowance, "Not Eligible for Allowance" will be display.
		- As per criteria meets, the increment will be provided to employee
		- This increment will be send to prev file to save in DB.
	- Further this script will check if any increment is received or not, because it may display any alert while calculating allowance.
	- if increment is returned it will redirect back to main menu.
	- Otherwise, the increment is also added to DB Script to insert the whole data in logs.
	- Data inserted into DB is commited now.
	- Connection closed with DB.
	- As per requirement, an Email will be send as per new records added to logs.
		- Here, 'email_automation.py' plays role. Function to send mail for new record is 'email_for_new()'
		- this function contains 'listofemails', 'sender_email'
		- SMTP plays huge role init.
		- i used yagmail lib, yagmail is a GMAIL/SMTP client that aims to make it as simple as possible to send emails.
		- 'enumerate()' function is used to send and display status of sending emails.
		-  After sending Emails, we return to main menu
	- Choice will keep prompting to user to perform next task.

# Choice:2 => Request to Export Details in Excel format

- To export the records in excel format i created this script.
- Uses xlsxwriter.workbook py lib
- Creates Workbook, Worksheet
- Writes attributes first to excel sheet [coloumns name]
- Connects with DB & exports all the data from DB via script
- The script output is stored in a variable mysel
- 'enumerate()' function works on it and appends the data to 'output.xlsx'.

# Choice:3 => Only on 15th & 22nd Day of Month
	
- In this, a py function 'trig()' is imported from a script 'date_trigger()'.
- This check the current day of month, if it is 15 or 22 day of month, 
	- an email automation will takes place.
	- from 'email_automation.py' using function 'alert_notif()'.
- if not 15 or 22 day of month
	- an alert 'Not Today !' will be displayed.

# Choice:4 => Update Records
	
- In this, a py function 'update()' is imported from a script 'date_trigger()'.
	- a new choice for updation will prompt to user [y/n]
	- [n] > alert of 'Nothing Updated => Good to Go.' will be displayed.
	- [y] > a py function 'up_xl()' is imported from a script 'update_xl' will be imported.
		- Here, it open the 'output.xlsx' with 'Sheet1'-Worksheet.
		- in while loop:
			- input the candidate number as per record in DB.
			- ask the following choice to update:
				- A - Name
				- B - Reporting_Manager
				- C - Project
				- D - Start_Date
				- E - Recurring
				- F - End_Date
				- G - Start_Time
				- H - End_Time
				- I - STOP
			- if choice == 'I': it will exit to main menu
			- if choice is other than listed : 'Invalid Choice' will be displayed.
			- if choice is from listed : a new value for that record for particular candidate will be ask to input.
	- and the following record will be updated.
	- at last the updated record file of excel will be saved.

# Choice:5 => Exit

- As per user done with his work, he can exit from script via console easily.
- A Signing Off alert will be displayed on Console.

# Python Libraries:

- datetime
- yagmail
- openpyxl
- time
- sqlite3
- csv
- xlsxwriter
- workbook

- install all the requirements from requirements.txt using 'pip install -r requirements.txt'
