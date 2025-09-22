#https://youtu.be/WTpGjPELHxo


import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("email.gmail.com","password")
subject="test python"
body=" i love python "
masssage="subject:{}\n\n{}".format(subject,body)
listadd=["mail1.gmail.com","mail2.gamil.com"]
ob.sendmail("email.gmail.com",listadd,masssage)
print("send mail")
ob.quit()