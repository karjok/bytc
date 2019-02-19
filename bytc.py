import random,time,os
import subprocess as sp
from threading import Thread as trd
def bann():
	os.system('clear')
	print('\033[92m'+'''

▄▄▄▄·  ▄· ▄▌▄▄▄▄▄▄▄▄ . ▄▄·       ·▄▄▄▄  ▄▄▄ .
▐█ ▀█▪▐█▪██▌•██  ▀▄.▀·▐█ ▌▪▪     ██▪ ██ ▀▄.▀·
▐█▀▀█▄▐█▌▐█▪ ▐█.▪▐▀▀▪▄██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄
██▄▪▐█ ▐█▀·. ▐█▌·▐█▄▄▌▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌
·▀▀▀▀   ▀ •  ▀▀▀  ▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀
----------------------------------------------
       Just For Fun by Karjok Pangesty

''')










bann()
teks = input('Text or Characters : ')
if teks == '':
	teks = '0100010110101101010101110101110101011001011101011'
tm = input('Speed (1-1000): ')
if tm =='':
	tm = '100'
cl = input('Color (g/r): ')
t = list(teks)
if cl == 'g':
	cl ='\033[92m'
elif cl == 'r':
	cl ='\033[91m'
else:
	cl == '\033[0m'
w = ['   ',' ','  ']
n = []
v = -1
for i in range(len(list(teks))):
	v +=1
	n.append(v)
def play_anim():
#	for i in t[random.choice(n)]:
#		t.insert(random.choice(n),random.choice(w))
#		replace(i,random.choice(w))
		random.shuffle(t)
		d=str(t)
		a = d.replace("'","")
		a = a.replace(",","")
		a = a.replace("[","")
		a = a.replace("]","")
		a = a.replace(str(t[random.choice(n)]),random.choice(w))
		a = random.choice(w).join(a)
		print(cl+a),;time.sleep(int(tm)/1000)

def play_sound():
	#for x in range(10):
	sp.call('mpv .whine',shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
try:
	bann()
	tr = trd(name='hehe',target=play_sound)
	tr.start()
	time.sleep(3)
	while tr.isAlive:
		play_anim()
except:
	exit()
