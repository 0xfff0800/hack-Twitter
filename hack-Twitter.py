import requests as s
import sys, os, time, signal, webbrowser, platform, subprocess
from time import sleep


def signal_handler(signal, frame):
		KURO()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
		time.sleep(2)
		EXITMENU()
signal.signal(signal.SIGINT, signal_handler)

#~~~ Function KURO ~~~~
def KURO():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')


#-------------------------------




def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')

print (' ')
ketik ("\033[1;36m Welcome to the integrated tool of hack Twitter I think over time it will be supported with a guess ....\033[1;36m")
sleep(0.5)

print ('''
       ===========    /////////////
          ====        |  twitter  |/
          ====        |-----------|/ 
          ====        |   falah   |/ 
          ====        | 0xfff0800 |/ 
          ====        |___________|/
>---------------------------------------->
Developer: 0xfff0800
snapchat:  flaah999
''')

base_url = 'https://twitter.com/users'
email_sub_url = '/email_available?email='
username_sub_url = '/username_available?username='




def check_email(email):
    email = email.replace(" ", "")
    try:
        response = s.get(base_url+email_sub_url+email)
        data = response.json()
        if data['valid'] is True:
            print(str(email)+" == Available!")
        elif data['valid'] is False:
            print(str(email)+" == Unavailable, " + data['msg'])
        else:
            print("Something wrong")
    except Exception as e:
        print("Something wrong " + str(e))



def check_username(username):
    username = username.replace(" ", "")
    try:
        if 4 < len(username) < 15:
            response = s.get(base_url+username_sub_url+username)
            data = response.json()
            if 'valid' in data:
                if data['valid'] is True:
                    print(str(username)+" == Available!")
                elif data['valid'] is False:
                    print(str(username)+" == Unavailable, "+data['msg'])
            else:
                print("Something wrong")
        else:
            print(str(username)+" == Sorry, Your username must be more than 4 and shorter than 15 characters")
    except Exception as e:
        print("Something wrong " + str(e))


def main():
    while True:
        print("\n>---------------------------------------->\n1 For Check Username"
              "\n2 For Check Email\n3 For Check username list\n4 For Check email list\n5 Search with images inside Twitter\n6 Save Twitter \n7 snapchat me falah ^_+ \nPress q to quit.\n\n")
        option = input("Your Option: ")
        if option == 'q' or option == 'Q':
            break
        elif option == '1':
            username = input("\nPlease enter the username: ")
            check_username(username)
        elif option == '2':
            email = input("\nPlease enter the email: ")
            check_email(email)
        elif option == '3':
            f = input("\nPlease enter the path your username file: ")
            try:
                username_file = open(f, 'r')
                username_list = username_file.read()
                for username in username_list.splitlines():
                    check_username(username)
            except Exception as e:
                print("Something wrong, "+str(e))
            else:
                username_file.close()
        elif option == '4':
            f = input("\nPlease enter the path of your email file: ")
            try:
                email_file = open(f, 'r')
                email_list = email_file.read()
                for email in email_list.splitlines():
                    check_email(email)
            except Exception as e:
                print("Something wrong, " + str(e))
            else:
                email_file.close()
        
        elif option == '5':
            username = input(" username: ")
            
            webbrowser.open('https://twitter.com/search?f=images&vertical=default&q='+username+'')
        
        elif option == '7':
            webbrowser.open('https://www.snapchat.com/add/flaah999')
        
        elif option == '6':
            webbrowser.open('https://download-twitter-videos.com/ar/')
        
            continue

if __name__ == '__main__':
    main()
