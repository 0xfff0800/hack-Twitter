import random
import sys
import os
import time

os.system("clear")
print("\033[1;36m Author   : Falah \033[1;36m")
time.sleep(2)
print("snapchat : flaah999")
time.sleep(1)
print("Twitter  : 0xfff0800")
time.sleep(1)




#================================================
#Domains that you need in the guess on the email
#(hotmail.com)
#(gmail.com)
#(outlook.sa)
#(Yahoo.com)
#================================================
uesr = 'rrr' #Type the username that appears on the authentication page, the first two characters, etc


chars2 = '1234567890' #Choose numbers or letters if desired
email = '@outlook.sa'#Choose a specific domain, for example, hotmail, depending on what appears on the credibility page
print('=========================================')
amount = input('How many passwords?')
amount = int(amount)
length2 = input('How long is the password you want?')
length2 = int(length2)

print('==================================')

for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)



    print (uesr+password+email)
    with open('password.txt', 'a') as x:
     x.write(uesr + password + email + '\n')
