import smtplib


def sendEmail(gmailAddress,
              gmailPassword,
              recipientAddress,
              message,
              smtpServer="smtp.gmail.com"):
    server = smtplib.SMTP(smtpServer, 587)
    server.starttls()
    server.login(gmailAddress, gmailPassword)
    server.sendmail(gmailAddress, recipientAddress, message)
    server.quit()
