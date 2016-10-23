import smtplib
from tkinter import *
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

root = Tk()

Sender = Label(root, text = "Enter Sender's E-Mail Address")
sending = Entry(root, bd = 5)
#fromaddren = bytes(sending.get(), "ascii")
#fromaddr = str(fromaddren.decode("ascii"))
#print(fromaddr)

reciver = Label(root, text = "Enter Reciver's E-Mail Address")
reciving = Entry(root, bd = 5)
#toaddren = bytes(reciving.get(), "ascii")
#toaddr = str(toaddren.decode("ascii"))
#print(toaddr)

sub = Label(root, text = "Enter Subject")
reason = Entry(root, bd = 5)
#subjecten = bytes(reason.get(), "ascii")
#subject = str(subjecten.decode("ascii"))
#print(subject)

def getInfo():
    #canvas.delete("all")
    fromaddr = sending.get()
    toaddr = reciving.get()
    subject = reason.get()
    
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = " "

    msg.attach(MIMEText(body, 'plain'))

    filename = "Calculator_Code.txt"
    attachment = open(r" ")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, " ")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

submit = Button(root, text ="Email", command = getInfo)

Sender.pack()
sending.pack()
reciver.pack()
reciving.pack()
sub.pack()
reason.pack()
submit.pack(side =BOTTOM) 
root.mainloop()
