import os, re,bs4,sys,json,bs4
import requests
from bs4 import BeautifulSoup as parser
import time
from datetime import datetime
ses=requests.Session()
time.sleep(3 /100)
M = '\x1b[1;91m' # MERAH			
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'	# WARNA MATI
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
freetoken = []
def mengetik(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3 /100)
        
def get_token():
	url = parser(ses.get("https://free.facebook.com/100040708001839/posts/716737126359881/?app=fbl").text,"html.parser")
	data = re.findall("EAA\w+",str(url))
	for token in data:
		try:
			if len(token)>=35:
				if token in freetoken:pass
				else:
					freetoken.append(token)
					print(f"""
 [+] Status : {cekstatus(token)}
 [+] Token  : {token}""")
		except:continue
def cekstatus(token):
	try:
		url = ses.get("https://graph.facebook.com/me?access_token={token}").json()
		data = f"{H}Aktif{N}"
	except KeyError:
		data = f"{M}Kadaluwarsa{N}"
	return data

IP = requests.get('https://api.ipify.org').text

def INTERNE():
	print("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] IP Kamu Saat Ini :",IP)

def banner():
	print(f"""
  {H}____ _____ _____   _____ ___  _  _______ _   _  __     __  _
 {H}/ ___| ____|_   _| |_   _/ _ \| |/ / ____| \ | | \ \   / / / |
{H}| |  _|  _|   | |     | || | | | ' /|  _| |  \| |  \ \ / /  | |
{O}| |_| | |___  | |     | || |_| | . \| |___| |\  |   \ V /_  | |
 {O}\____|_____| |_|     |_| \___/|_|\_\_____|_| \_|    \_/(_) |_|\n
 """)

def menu():
	print (f"""
\x1b[1;97m[\x1b[1;92m1\x1b[1;97m] Get Token Facebook
\x1b[1;97m[\x1b[1;92m2\x1b[1;97m] Script CrackFB Gratis
\x1b[1;97m[\x1b[1;92m3\x1b[1;97m] Script Spam
{P}[4].{M} exit
""")

def tanya():
	mana = input("\x1b[1;97mPilihan : \x1b[1;92m")
	if mana == "1":
		print("Sabar Tod")
		get_token()
		input("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Tekan Enter Unuk Kembali...")
		os.system("clear")
		banner()
		INTERNE()
		menu()
		tanya() 
	elif mana == "2":
		print("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Install Bahan\n")
		mengetik ("pkg update && pkg upgrade")
		mengetik("pkg install python")
		mengetik("pip install requests")
		mengetik("pip install futures")
		mengetik("pip install bs4")
		mengetik("pkg install git")
		mengetik("git clone https://github.com/CyberCarboon/crackFB\n")
		print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Menjalankan\n')
		mengetik("ls")
		mengetik("cd crackFB")
		mengetik("python cracker.py\n")
		print("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] Done..!\n")
		input("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] Tekan Enter Untuk Kembali.....")
		os.system("clear")
		banner()
		INTERNE()
		menu()
		tanya() 
	elif mana == "3":
		print("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Install Bahan\n")
		mengetik("pkg update && pkg upgrade")
		mengetik("pkg install python")
		mengetik("pkg install python2")
		mengetik("pip install requests")
		mengetik("pkg install bash")
		mengetik("pkg git")
		mengetik("git clone https://github.com/CyberCarboon/kang-spam\n")
		print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Menjalankan\n')
		mengetik("cd kang-spam")
		mengetik("python spamV2.py\n")
		print("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] Done..!\n")
		input("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] Tekan Enter Untuk Kembali.....")
		os.system("clear")
		banner()
		INTERNE()
		menu()
		tanya() 
	elif mana == "4":
		print("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Terima Kasih Ngab !")
		os.system("exit")
		
		

if __name__ == '__main__':
	os.system("clear")
	banner()
	INTERNE()
	menu()
	tanya()


