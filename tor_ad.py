import dri_mod
import ok
import time
from pyvirtualdisplay import Display


# def visit_tor():
# 	for i in range(5):
# 		print(ok.get_current_ip())
# 		ok.renew_tor_ip()
# 		time.sleep(5)

url_y="https://30m30m.nl.eu.org/"

def visit_tor(driver):
	print(ok.get_current_ip())
	ok.renew_tor_ip()
	driver.get(url_y)
	print(ok.get_current_ip())
	time.sleep(25)
	driver.delete_all_cookies()
	driver.quit()




if __name__ == "__main__":
	try:
		print("gj")
		display = Display(visible=0, size=(dri_mod.width,dri_mod.height)).start()
		driver=dri_mod.build_driver()
		visit_tor(driver)
		display.stop()

		print("starting")
	except Exception as error:
		print("except "+str(error))
	dri_mod.cleanx()