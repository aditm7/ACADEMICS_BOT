from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

#inputting the user id and password
id = ""
pas = ""

def main1(url):
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()
	#ouputting the user data in respective feilds
	try:
	    main = WebDriverWait(driver, 5).until(
	        EC.presence_of_element_located((By.ID, "login"))
	    )    
	    username = driver.find_element_by_id("username")
	    password = driver.find_element_by_id("password")  
	    username.send_keys(id)
	    password.send_keys(pas)  

	    #solving the captcha
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

	    #clicking the final submit button
	    j = driver.find_element_by_id("valuepkg3")
	    j.clear()
	    j.send_keys(c)
	    button = driver.find_element_by_id("loginbtn")
	    button.click()

	except:
		t=5
if sys.argv[1] == "ELL":
	main1("https://moodle.iitd.ac.in/course/view.php?id=11053")
elif sys.argv[1] =="ELP":
	main1("https://moodle.iitd.ac.in/course/view.php?id=11713")
elif sys.argv[1] =="PYL":
	main1("https://moodle.iitd.ac.in/course/view.php?id=11358")
elif sys.argv[1] =="MTL":
	main1("https://hkkaushik.wordpress.com/courses/")
elif sys.argv[1] =="COL":
	main1("https://www.cse.iitd.ac.in/~aseth/col100-2021/col100.html")
else:
	print("please run the command in this format: python moodle.py coursecode")



