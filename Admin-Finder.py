# Script feito por: Nano
# Telegram: https://t.me/rdzin9

import os
import sys
import re
import requests
import datetime
import pathlib
from time import sleep

def LimparTela():

	global system
	system = sys.platform

	match system:
		case "win32":
			os.system("cls")
		case "linux":
			os.system("clear")

def ValidEnter(msg=None):

	validar = re.search(r"^(http://|https://){1}(.)+(\/)$", msg, flags=re.IGNORECASE)
	if validar != None:
		return True
	else:
		return False

def ValidWay(way=None):

	way_valid = re.search(r"^((C:\\|/)?)([a-zA-Z0-9])+(\\|/){1}[a-zA-Z0-9]+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+\.(txt)$", way)
	if way_valid != None:
		return True
	else:
		return False

Persist = requests.Session()

LimparTela()
print("""\033[1;31m
                                       
		  ,---.     ,--.          ,--.         
		 /  O  \  ,-|  |,--,--,--.`--',--,--,  
		|  .-.  |' .-. ||        |,--.|      \ 
		|  | |  |\ `-' ||  |  |  ||  ||  ||  | 
		`--' `--' `---' `--`--`--'`--'`--''--' 
		,------.                        ,--.   
		|  .--. ' ,--,--.,--,--,  ,---. |  |   
		|  '--' |' ,-.  ||      \| .-. :|  |   
		|  | --' \ '-'  ||  ||  |\   --.|  |   
		`--'      `--`--'`--''--' `----'`--'   
                                       \033[m
		   \033[31m[*]\033[m\033[1m Scaner of admin page in websites\033[m
		   \033[31m[*]\033[m\033[1m Coded by: \033[m\033[1;36mNano\033[m
	           \033[31m[*]\033[m\033[1m Telegram: https://t.me/rdzin9\033[m
	           \033[31m[*]\033[m\033[1m Save in: \033[m\033[1;33mFound.txt \033[m

			      \033[1mVersion 1.2\033[m

\033[1;36m[!]\033[m \033[1mEXEMPLO URL: https://example.com/\033[1m

""")

site = str(input("\033[1;32m[+] Informe o site alvo:\033[m "))
wordlists = str(input("\033[1;32m[+] Você deseja utilizar a wordlist padrão? (Y/N)\033[m ")).strip().lower()
match = False

options = [

			"Y",
			"N",
			None

]

headers = {

'user-agent': 'Googlebot'
                      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.103 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1; rv:45.0)'
                      'Gecko/20100101 Firefox/45.0'
}

verify = ValidEnter(msg=site)
if not verify:
	print("\033[1;31m[!]\033[m \033[1mVerifique se a url digitada está correta! E não esqueça de adicionar -> / no final da url!\033[m\n")
else:
	try:
		site_teste = Persist.get(site)
	except requests.ConnectionError:
		print("\033[1;31m[!]\033[m \033[1mO Site não está disponível!\033[m\n")
		sys.exit()
	except KeyboardInterrupt:
		print("\033[1;31m[!]\033[m \033[1mSaindo...!\033[m\n")
		sleep(0.5)
		sys.exit()
	else:
		if site_teste.status_code == 200:

			if wordlists == "y":

				size = open("admin.txt","r")
				wordlist_size = len(size.read())
				print("\n\033[1;36m[*]\033[m \033[1;32mCarregado\033[m \033[1;33m{}\033[m \033[1;32murl na wordlist!\033[m".format(wordlist_size))
				size.close()
				sleep(1)
				print("\033[1;36m[*] \033[m\033[1;32mIniciado as\033[m \033[1;33m{}\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
				start = datetime.datetime.now()
				with open("admin.txt","r") as page:
					for pages in page:
						admin_page = pages.replace("\n","")
						testar = site+admin_page.strip().lower()
						try:
							conectar = Persist.get(testar,headers=headers)
						except KeyboardInterrupt:
							print("[×] Saindo...")
							sleep(0.5)
							sys.exit()
						except requests.ConnectionError:
							print("\033[1;31m[!] url indisponível!\033[m")
							sys.exit()
						else:
							if conectar.status_code == 200:
								finish = datetime.datetime.now() - start
								result = str(finish)
								match = True
								print("\n\033[1;33m-----------------------------\033[m")
								print("\033[1;36M[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
								print("\033[1;36M[INFO]\033[m \033[1;32mAdmin Page: :\033[m \033[1m{}\033[m".format(testar))
								print("-----------------------------\033[m\n")
								with open("Found.txt","a") as save1:
									save1.write("-----------------\n")
									save1.write("SITE: {}\n".format(site))
									save1.write("Página de Adm: {}\n".format(testar))
									save1.write("-----------------\n")
									save1.close()
							else:
								print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar.status_code,testar))
					page.close()

				if not match:
					print("\n\033[1;33m[{}] \033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m".format(datetime.datetime.now().strftime("%H:%M:S")))

			elif wordlists == "n":
				caminho_wordlist = str(input("\033[1;33m[+] Informe o caminho + nome da wordlist: \033[m")).strip()
				exists = ValidWay(way=caminho_wordlist)
				if exists:
					size2 = open(caminho_wordlist,"r")
					wordlist_size2 = len(size2.read())
					print("\n\033[1;36m[*]\033[m \033[1;32mCarregado\033[m \033[1;33m{}\033[m \033[1;32murl na wordlist!\033[m".format(wordlist_size2))
					size2.close()
					print("\033[1;36m[*] \033[m\033[1;32mIniciado as\033[m \033[1;33m{}\033[m\n".format(datetime.datetime.now().strftime("%H:%M:%S")))
					starts = datetime.datetime.now()
					try:
						with open(caminho_wordlist,"r") as page2:
							for pages2 in page2:
								admin_page2 = pages2.replace("\n","")
								testar2 = site+admin_page2.strip().lower()
								try:
									conectar2 = Persist.get(testar2,headers=headers)
								except KeyboardInterrupt:
									print("[×] Saindo...")
									sys.exit()
								except requests.ConnectionError:
									print("\033[1;31m[!] url indisponível!\033[m")
									sys.exit()
								else:
									if conectar2.status_code == 200:
										finishs = datetime.datetime.now() - starts
										results = str(finishs)
										match = True
										print("\n\033[1;33m-----------------------------\033[m")
										print("\033[1;36M[INFO]\033[m \033[1;32mSITE:\033[m \033[1m{}\033[m".format(site))
										print("\033[1;36M[INFO]\033[m \033[1;32mAdmin Page: :\033[m \033[1m{}\033[m".format(testar2))
										print("-----------------------------\033[m\n")
										with open("Found.txt","a") as save:
											save.write("-----------------\n")
											save.write("SITE: {}\n".format(site))
											save.write("Página de Adm: {}\n".format(testar2))
											save.write("-----------------\n")
											save.close()
									else:
										print("\033[1;33m[{}]\033[m \033[1;31m[{}]\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar2.status_code,testar2))
							page2.close()
							if not match:
								print("\n\033[1;33m[{}]\033[m\033[1;31m[NOT FOUND]\033[m \033[1;32mNenhuma página de adminstrador encontrada!\n\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					except FileNotFoundError:
						print("\033[1;31m[!] Arquivo {} não encontrado!\033[m".format(caminho_wordlist))
						sys.exit()
				else:
					if system == "win32":
						print("\033[1;31m[!]\033[m \033[1mVerifique se o caminho começa com C:\\\n\033[1;31m[!]\033[m e contém o nome do arquivo com final .txt e tente novamente!\033[m\n")
					elif system == "linux":
						print("\033[1;31m[!]\033[m \033[1mVerifique se o caminho começa com /\n\033[1;31m[!]\033[m e contém o nome do arquivo com final .txt e tente novamente!\033[m\n")
#end
