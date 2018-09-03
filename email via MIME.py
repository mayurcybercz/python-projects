from email.mime.text import MIMEText
import smtplib
msg=MIMEText("hello there,this email is sent via python ")
msg['Subject']=input("write the body of the email")
msg['From']='<rahangdalemayur@gmail.com>'
msg['To']='<rahangdal640@gmail.com>'
print("message composed,sending now ")

s=smtplib.SMTP('smtp.gmail.com')
s.sendmail('rahangdalemayur@gmail.com',['rahangdale640@gmail.com'],msg.as_string())
print("email sent!")
