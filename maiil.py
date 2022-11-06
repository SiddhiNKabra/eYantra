import  smtplib
from email.message import EmailMessage


def email(sub, body ,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
    msg['to'] = to
    user = 'testmailservice2718@gmail.com'
    msg['from'] = user
    pw = "ppinmdacydlilfpx"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,pw)
    server.send_message(msg)
    server.quit()

l = ['anishpurupawar@gmail.com','knj1507@hotmail.com','nksiddhi20@gmail.com','saniyaatalatti05@gmail.com']
for i in l:
    email('Test mail', 'Hello World', i)
