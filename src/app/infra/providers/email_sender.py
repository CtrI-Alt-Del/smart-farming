import smtplib
from core.commons import Error 
import email.message

class EmailProvider:
    def __init__(self):
        self.data = None



    def send_email(sender,receiver,template,password):
        try:
            email_body = template
            msg = email.message.Message()
            msg['Subject'] = 'Ctrl Alt Del team'
            msg.add_header('Content-Type','text/html')
            msg.set_payload(email_body)
            

            s = smtplib.SMTP('smtp.gmail.com:587')

            s.starttls()
            s.login(sender,password)
            s.sendmail(sender,receiver,msg.as_string().encode('utf-8'))
        except smtplib.SMTPAuthenticationError as e:
            print(f"Failed to authenticate: {e}")
        except Error as e:  
            raise Error(ui_message=e,internal_message="catapimas")
