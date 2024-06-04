import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self,sender,receiver,template_path,password):
        try:
            with open(template_path, 'r') as file:
                html_content = file.read()

            email_body = template_path
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Ctrl Alt Del team'
            
            part1 = MIMEText(html_content,"html")
            msg.attach(part1)

            s = smtplib.SMTP('smtp.gmail.com:587')

            s.starttls()
            s.login(sender,password)
            s.sendmail(sender,receiver,msg.as_string().encode('utf-8'))
        except smtplib.SMTPAuthenticationError as e:
            print(f"Failed to authenticate: {e}")
        except Exception as error:
            print(f"Toma o erro {error} ")


    






