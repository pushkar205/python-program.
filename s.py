# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "EMAIL address of the sender"
toaddr = "EMAIL address of the receiver"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail 
body = "Body_of_the_mail"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 


filename = "File_name_with_extension"
attachment = open("Path of the file", "rb") 


p = MIMEBase('application', 'octet-stream') 


p.set_payload((attachment).read()) 


encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


msg.attach(p) 


s = smtplib.SMTP('smtp.gmail.com', 587) 


s.starttls() 


s.login(fromaddr, "Password_of_the_sender") 


text = msg.as_string() 

 
s.sendmail(fromaddr, toaddr, text) 


s.quit() 
