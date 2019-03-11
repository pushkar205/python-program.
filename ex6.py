import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='pritamchaurasiya11@gmail.com'
	receiver='puskrsuman@gmail.com'
	msg="peace!!!!"
	s.login(sender,'ddmmjbP5@123')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("message sent succesfully")
	s.quit ()