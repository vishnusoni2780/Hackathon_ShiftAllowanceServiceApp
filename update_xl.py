def up_xl():
	import openpyxl
	import time

	file = openpyxl.load_workbook('output.xlsx')
	sheet = file.get_sheet_by_name('Sheet1')

	while True:

		cand_no=input("\n[Check the DB Table]\nWhich record you want to update [candidate's number]: ")
		cand_no=str(int(cand_no)+1)
		print("""\nwhat you want to update, Please select choice:
		
		A - Name
		B - Reporting_Manager
		C - Project
		D - Start_Date
		E - Recurring
		F - End_Date
		G - Start_Time
		H - End_Time
		I - STOP
		""")

		upd_choice=input("Choice: ")
		upd_choice=upd_choice.upper()

		if upd_choice=='I':
			break
		
		elif upd_choice not in ['A','B','C','D','E','F','G','H']:
			print("\nInvalid Choice.")
			time.sleep(2)
		
		else:
			new_val=input("\nEnter the New value of Record: ")

			if upd_choice=='A':
				sheet['A'+cand_no]=new_val
			elif upd_choice=='B':
				sheet['B'+cand_no]=new_val
			elif upd_choice=='C':
				sheet['C'+cand_no]=new_val
			elif upd_choice=='D':
				sheet['F'+cand_no]=new_val=new_val
			elif upd_choice=='E':
				sheet['G'+cand_no]=new_val
			elif upd_choice=='F':
				sheet['H'+cand_no]=new_val
			elif upd_choice=='G':
				sheet['I'+cand_no]=new_val
			elif upd_choice=='H':
				sheet['J'+cand_no]=new_val

			file.save('output.xlsx')
			print("\nData Saved.")
			time.sleep(2)

	return True