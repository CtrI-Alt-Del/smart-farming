from smtplib import SMTP, SMTPAuthenticationError
from core.commons import Error
from email.message import Message


class EmailProvider:
    def send_email(sender: str, receiver: str, template: str, password: str):
        try:
            email_body = template
            msg = Message()
            msg["Subject"] = "Ctrl Alt Del team"
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(email_body)

            smtp = SMTP("smtp.gmail.com:587")
            smtp.starttls()
            smtp.login(sender, password)

            smtp.sendmail(sender, receiver, msg.as_string().encode("utf-8"))
        except SMTPAuthenticationError as error:
            raise Error(ui_message="app password errada", internal_message=error)
