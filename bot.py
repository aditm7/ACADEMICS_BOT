from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

#inputting the user id and password
moodle_id = "ee1200458"
moodle_password = "426d7d31"
impartus_id = "ee1200458@ee.iitd.ac.in"
impartus_password = "adit2348"


#function for wrong format entered
def exit(message):
  print(message)
  sys.exit(1)

#function to handle moodle links
def moodle(url):
	#intialising driver
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()
	main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
	#entering id and pass
	username = driver.find_element_by_id("username")
	password = driver.find_element_by_id("password")
	username.send_keys(moodle_id)
	password.send_keys(moodle_password)  


	#captcha solving
	l=main.text.split("\n")
	t=l[3]
	s=t.split(" ")
	if s[1]=="add":
		c = int(s[2]) + int(s[4])
	elif s[1]=="subtract":
		c = int(s[2]) - int(s[4])
	elif s[2]=="first" :
		c = int(s[4]) 
	elif s[2]=="second":
	    c = int(s[6])

	j = driver.find_element_by_id("valuepkg3")
	j.clear()
	j.send_keys(c)
	button = driver.find_element_by_id("loginbtn")
	button.click()


#function to handle impartus links
def impartus(url):
	#initialising driver
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()
	driver.implicitly_wait(5)
	
	#inputting the user id and password
	username = driver.find_element_by_xpath("//input[@id='username']")
	password = driver.find_element_by_xpath("//input[@id='password']")
	username.send_keys(impartus_id)
	password.send_keys(impartus_password)
	button = driver.find_element_by_xpath("//div[@class='iu-btn iu-btn-wt']")
	button.click()


#function to handle coursewebpage links
def coursewebpage(url):
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()


def main():
	#if wrong format of arguments are entered
	len_arg = len(sys.argv)
	if len_arg!=3:
		sys.exit('usage: bot.py <1_letter_moodle(m)/impartus(i)/coursepage(c)> [3_letter_coursecode]')

	#if the choice is moodle
	code = sys.argv[2]
	if sys.argv[1]=='m' or sys.argv[1]=='M':
		url_1 = "https://moodle.iitd.ac.in/course/view.php?id="
		if code == "ELL" or code == "ell":
			moodle(url_1 + "11053")
		elif code == "ELP" or code == "elp":
			moodle(url_1 + "11713")
		elif code == "PYL" or code == "pyl":
			moodle(url_1 + "11358")
		elif code == "COL" or code == "col":
			moodle(url_1 + "10887")
		elif code == "MTL" or code == "mtl":
			moodle(url_1 + "11626")
		else:
			print("Invalid CourseCode")

#if the choice is impartus
	elif sys.argv[1] == 'i' or sys.argv[1] == 'I':
		url_1 = "https://a.impartus.com/ilc/#/course/"
		if code == "ELL" or code == "ell":
			impartus(url_1 + "1142252/456")
		elif code == "ELP" or code == "elp":
			impartus(url_1 + "1229930/456")
		elif code == "PYL" or code == "pyl":
			impartus(url_1 + "1142557/456")
		elif code == "COL" or code == "col":
			impartus(url_1 + "1142086/456")
		elif code == "MTL" or code == "mtl":
			impartus(url_1 + "1226397/456")
		else:
			print("Invalid CourseCode")

#if the choice is coursewebpage
	elif sys.argv[1] == 'c' or sys.argv[1] =='C':
		if code == "COL" or code == "col":
			coursewebpage("https://www.cse.iitd.ac.in/~aseth/col100-2021/col100.html")
		elif code == "MTL" or code == 'mtl':
			coursewebpage("https://hkkaushik.wordpress.com/courses/")
		else:
			print("the course webpage not found")
	
#if the choice is backpack view for impartus
	elif sys.argv[1] == 'bp' or sys.argv[1] == "BP":
		impartus("https://a.impartus.com/ilc/#/gbackpack")

if __name__ == "__main__":
  main()



