import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("supriyoghatak15@gmail.com","7501374121")


subject = "Sending Email Using Python"

body = "Hi this is a mini project made by me just reply me how it is just trying to pass time................"

message="Subject:{}\n\n{}".format(subject,body)

listOfAd = ["supriyo.ghatak.cse21@heritageit.edu.in","tanmoy.das.cse21@heritageit.edu.in","amrita.pal.cse21@heritageit.edu.in"]

ob.sendmail("supriyoghatak15", listOfAd, message)

print("send Suc")

ob.quit();

