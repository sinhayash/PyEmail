import smtplib


def sendEmail(gmailAddress,
              gmailPassword,
              recipientAddress,
              message,
              smtpServer="smtp.gmail.com", 
              port=587):
    server = smtplib.SMTP(smtpServer, port)
    server.starttls()
    server.login(gmailAddress, gmailPassword)
    server.sendmail(gmailAddress, recipientAddress, message)
    server.quit()
