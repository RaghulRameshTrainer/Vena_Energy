import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_address='pythonweekday22@gmail.com'
to_address='pythonweekday22@gmail.com'
subject='Daily Status Report'

msg=MIMEMultipart()
msg['from']=from_address
msg['to']=to_address
msg['Subject']=subject

body="Hello Everyone! \n Please find the attachment for the today's report.\n Thanks!\nIT Team"
msg.attach(MIMEText(body,'plain'))

filename=r'C:\Users\RaghulRamesh\OneDrive\Desktop\ETL\company_data.csv'
atatchment=open(filename,'r')

part = MIMEBase('application', 'octet-stream')
part.set_payload((atatchment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachmemt: filename="+filename)

msg.attach(part)
x=msg.as_string()
connection=smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login(from_address,'Funnypass@123')
connection.quit()