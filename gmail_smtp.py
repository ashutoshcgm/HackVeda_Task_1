from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
import os

email_sender= 'ashutoshsinghparihar@gmail.com'
sender_address_name= "Ashutosh <ashutoshsinghparihar@gmail.com>"
email_password= "ENTER PASSWORD"
email_receiver=input("Enter the email id of the receipt.")

Subject= "Regarding Intership"
Body="""Dear Sir/Madam
Myself Ashutosh I applied on your company for summer intership program.
I am eager to know to know the status of my application.
Thanking you
Ashutosh Singh"""

em=EmailMessage()
em['From']= email_sender
em['To']=email_receiver
em['subject']=Subject
em.set_content(Body)

attachment_path = "/content/AshutoshSinghResume.pdf"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
with open(attachment_path, 'rb') as ap:
      em.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                             filename=os.path.basename(attachment_path))

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())