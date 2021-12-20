from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time
import smtplib   # for sending Email

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("my-project-first-api-using-fc31959b9385.json", scope)

client = gspread.authorize(creds)

python_test = client.open("fatih-api-project").sheet1

counter = 2

E_Mail = []

content = "Welcome... our company..." # for sending Email

mail = smtplib.SMTP("smtp.gmail.com", 587) # for sending Email
mail.ehlo() # for sending Email
mail.starttls() # for sending Email
mail.login("your email address", "your email password") # for sending Email

while True:

    test1 = python_test.cell(counter,5)


    if test1.value and not test1 in E_Mail: # test1.value =  Email address that you want to send a Email

        mail.sendmail("your email address",f"{test1.value}",content) # for sending Email

        print(f"Ailemize {test1.value} katildi...")

        E_Mail.append(test1.value)

        counter += 1

    else:
        print("Yeni giris yoktur!!!")
    time.sleep(10)