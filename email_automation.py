"""
->	Made a new Gmail account
->	used "yagmail" py. lib. to make process easy and smooth. password is require once for 'keyring' only.
	because using SMTP server we need to turn on the "Allow less secure apps" which is not good at all.
->	More details will be shared as per update.

test gmail account:
email = pythontestforproject@gmail.com
pw = <>

email_addr= input("Sender's Email: ")
passwd= input("Sender's password: ")
rec_email=input("Receiver's Email: ")
"""
def email_for_new():
	import yagmail
	import time

	# Default Params
	listofemails=["vishnusoni632@gmail.com","vanshprajapat165@gmail.com","vishnu.soni@intimetec.com"]
	sender_email="pythontestforproject@gmail.com"

	# Descriptive msgs
	subj="Shift Allowance Service App"
	body="Hello, a new shift record is added to the system."
	# Sending.
	print("\nSending Email...")
	yag=yagmail.SMTP(sender_email)
	for i,receiver_email in enumerate(listofemails):
		yag.send(
			to=receiver_email,
			subject=subj,
			contents=body,
#**			attachments=report
			)
		print("Email Sent to {} -> {}".format(i+1,receiver_email))

	print("\nEmail Sent to all.")
	time.sleep(2)
	return True

def alert_notif(d):
	import yagmail
	import time
#**	report=''

	# Default Params
	listofemails=["vishnusoni632@gmail.com","vanshprajapat165@gmail.com"]
	sender_email="pythontestforproject@gmail.com"

	# Descriptive msgs
	subj="Email notification for Update."
	body="Hello, please update the records for reportees it's {} of month".format(d)

	# Sending.
	print("\nSending Email...")
	yag=yagmail.SMTP(sender_email)
	for i,receiver_email in enumerate(listofemails):
		yag.send(
			to=receiver_email,
			subject=subj,
			contents=body,
#**			attachments=report
			)
		print("Email Sent to {} -> {}".format(i+1,receiver_email))

	print("\nEmail Sent to all.")
	time.sleep(2)
	return True
