import time
from datetime import datetime
current_time = datetime.now()
bankname = "[Change Me!]"
businessname = "[Change Me!]"
balance = "[Change Me!]"
ctime = datetime.now()
print(f"Welcome to the online backing server for {bankname}. \nPlease use the email: Penatration@notemails.com")
email = input("Please Enter Your Email: ")
semail = "imascammer@outlook.com"
if email > chr(10):
    print(f"Connecting to {email}")
    print(f"Welcome to {bankname}, please wait while we connect to our closest branch")
    time.sleep(15)
    print(f"Current balance is set at: {balance}")
    print(f"Reviewing Recent Transactions... :\n{current_time}: 40,000 from your account - {businessname}")
    print("Please confirm you are the owner of said account.")
    name = input("Enter You're Full Name: ")
    dateofbirth = input("Please confirm you're Date of Birth: ")
    file = open(f"{name} - {bankname} details.txt", "x")
    file.write(f"Record at {ctime}")
    file.write(f"\nEmail: {email}")
    file.write(f"\nBank: {bankname}")
    file.write(f"\nName: {name}")
    file.write(f"\nDate Of Birth: {dateofbirth}")
    file.write(f"\n Recent Transactions:\n 40,000 sent to ****{businessname}****\n26,000 to Linux")
    file.write(f"\nThanks for Using {bankname}'s Online Banking Server, All data will be kept GDPR Complient.")
    file.close()
    print("Authorised")
    time.sleep(3)
    print(f"Most recent payment of $40,000 made out to {businessname}")
    time.sleep(5)
    print(f"Check our folder, you should have recieved a text file please email this to: {semail}.\nCLOSING BANK SERVER. PLEASE WAIT")
    time.sleep(2)
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    print("Successful Shutdown")