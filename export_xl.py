def exp_xl():
    import sqlite3
    from xlsxwriter.workbook import Workbook
    import time, os

    if os.path.isfile('output.xlsx')==False:
        print("\nCreating Workbook...")
        time.sleep(2)
        workbook = Workbook('output.xlsx')
        print("Workbook Created.")
        time.sleep(1)

        print("\nCreating Worksheet...")
        time.sleep(2)
        worksheet = workbook.add_worksheet()
        print("Worksheet Created.")
        time.sleep(1)

        print("\nWriting Attributes to your Excel Sheet...")
        time.sleep(2)
        #for fields
        r,c=0,0
        fields=['Name', 'Reporting_Manager', 'Project', 'Location', 'Gender', 'Start_Date', 'Recurring', 'End_Date', 'Start_Time', 'End_Time', 'Allowance%']
        for i in fields:
            worksheet.write(r,c,i)
            c+=1

    else:
        print("\nAppending Records to existing file.")
        time.sleep(2)
        workbook = Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()

    print("\nConnecting to SQLite DB...")
    time.sleep(2)
    conn=sqlite3.connect('logs.sqlite')
    c=conn.cursor()

    c.execute("select * from DATA")
    mysel=c.execute("select * from DATA ")
    print("\nExporting in Progress...")
    time.sleep(2)

    for i, row in enumerate(mysel,1):
        for j, value in enumerate(row,):
            worksheet.write(i, j, row[j])
    workbook.close()
    conn.close()

    print("\nData Exported.")
    time.sleep(2)

    return True