import yagmail

l = ["vanshprajapat165@gmail.com","vishnusoni632@gmail.com"]
body = "Hello there from Yagmail"

yag = yagmail.SMTP("pythontestforproject@gmail.com")
for receiver in l:
	yag.send(
	    to=receiver,
	    subject="Yagmail test with attachment",
	    contents=body, 
	)
	
"""
import smtplib as sl
import time
server= sl.SMTP("smtp.gmail.com",587)
server.starttls()

mail = "pythontestforproject@gmail.com"
pw = "passwd@pythontest*"
#rec_email = "vanshprajapat165@gmail.com"

subject= "Testing of sending mail through python"
body = "Hello, mail from python script :)"
msg="Subject:{}\n\n{}".format(subject,body)

#l=["vanshprajapat165@gmail.com","vishnusoni632@gmail.com"]

server.login(mail,pw)
print("Login successfully.\n")

server.sendmail(mail, "vishnusoni632@gmail.com", msg)
#print("Sending Mail to {}\n".format(rec_email))

time.sleep(2)
print("Mail Sent to All.\n")
#print("Mail send to "+ rec_email+" successfully.\n")
time.sleep(1.5)

print("off to server.\n")
server.quit()

print("Have a Good day.")
"""