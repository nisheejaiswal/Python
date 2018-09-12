import smtplib

content = 'example email stuff here'

Server = smtplib.SMTP('smtp.gmail.com', 587)
Server.starttls()

Server.login("jaiswalnishee2@gmail.com","Papa11.09.1996")

Server.sendmail('jaiswalnishee2@gmail.com','nishee.jaiswal@gslab.com', content)
print("Email send Successfully")
Server.quit()