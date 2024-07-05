from flask import Flask
from flask import request
import smtplib
from email.message import EmailMessage

def sendEmail(textfile):
    
    smtp_user = "myemail@gmail.com"
    smtp_password = "mygmailapppassword" # you should create an App password from the google setting and replace it with this
    server = "smtp.gmail.com"
    port = 587
    to_address = 'user@gmail.com'

    msg = EmailMessage()
    msg['Subject'] = f'The contents of {textfile}'
    msg['From'] = smtp_user
    msg['To'] = to_address

    s = smtplib.SMTP(server, port)
    s.connect(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, to_address, msg.as_string())
    s.quit()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    sendEmail(request.get_json()['text'])
    return "email sent succesfully"

app.run("127.0.0.1",3000)