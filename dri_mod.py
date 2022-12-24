import os
import cnf_bvb
import emoji
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import random,datetime,string , os ,time ,subprocess , sys , requests ,re


def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i tor | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver-30 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("rm -rf __pycache__/")
		# os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("rm -rf /tmp/*")
		# os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		time.sleep(5)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")



def cleanx():
	
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver-30 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf __pycache__/")
		os.system("rm geckodriver.log")
		# os.system("ps aux | grep -i tor | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		# time.sleep(5)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")


init_fire()
arrrr=cnf_bvb.creat_session()
# print(arrrr)
width=arrrr[0]
height=arrrr[1]
myProxy = "localhost:9050"
ip, port = myProxy.split(':')




def build_driver():
	print(arrrr)
	print("BUILDING PROFILE DRIVER  ...... ",end='')
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)
	new_binary_path = arrrr[2]
	new_gecko_path = arrrr[3]
	# print(moz_hig,moz_wid)
	try:
		serv = Service(new_gecko_path)
		fp = webdriver.FirefoxProfile()
		ops = Firefox_Options()
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
		fp.set_preference('network.proxy.type', 1)
		fp.set_preference('network.proxy.socks', ip)
		fp.set_preference('network.proxy.socks_port', int(port))
		fp.set_preference('useAutomationExtension', False)
		fp.set_preference("security.sandbox.content.level", 0)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.set_preference("intl.accept_languages", "en-GB")
		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.maximize_window()
		print(emoji.emojize("Ok DRIVER "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
	return driver


# build_driver()