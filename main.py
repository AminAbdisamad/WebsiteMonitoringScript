import config
import smtplib
import requests

# Configurations
USER_EMAIL = config.USER_EMAIL
DEVICE_PASS = config.DEVICE_PASS 
WEBSITE = config.WEBSITE

r = requests.get("", timeout=5)
if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(USER_EMAIL,DEVICE_PASS)
            # Email Subject
        subject = "SOMETHING WENT WRONG WITH YOUR WEBSITE!!"
        body = "Your Website is down please check, backup and restart the server"
        msg = "Subject: {} \n\n {}".format(subject,body)
        smtp.sendmail(USER_EMAIL,'theaminux@gmail.com',msg)


