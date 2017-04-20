#!/usr/bin/env python


COMMAND = "ls -la" 
EMAIL = "name@gmail.com"
PASSWORD = "password"

from subprocess import check_output
import smtplib

output = check_output("ls -la", shell=True)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL, PASSWORD)
message = " ** Z Repporter ** \n"
message = message + "Result of " + COMMAND + "\n"
server.sendmail(EMAIL, EMAIL, message + output)
server.quit()