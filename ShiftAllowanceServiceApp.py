import time
while True:
	print("\n")
	print("-"*40)
	print("-: Service Allowance Service Console App :-")
	print("-"*40)
	print("""\nEnter your choice:

		1. Enter New Shift Record
		2. Request to Export Details in Excel format
		3. Only on 15th & 22nd Day of Month
		4. Update Records
		5. Exit

		""")
	print("-"*40)

	choice=int(input("\nChoice: "))

	if choice==1:
		import record_input_db as ri_db
		ri_db.record()

	elif choice==2:
		import export_xl as exxl
		exxl.exp_xl()

	elif choice==3:
		import date_trigger as dt
		dt.trig()
	
	elif choice==4:
		import date_trigger as dt
		dt.update()

	elif choice==5:
		print("\nSigning Off...")
		time.sleep(2)
		break

	else:
		print("\nInvalid choice...")
		time.sleep(2)