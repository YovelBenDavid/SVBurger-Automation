import time
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(r'C://selenium//chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()


def test_sanity(setup): #Sanity
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your first name']").send_keys("Yovell")
    driver.find_element_by_xpath("//input[@placeholder='Type your last name']").send_keys('Bennnn')
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("//button[text()='Send']").click()
    assert driver.find_element_by_xpath("//h2[text()='64.9']").is_displayed() == True

#Login Page Functionality tests:
#1:
def test_log_in(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    assert driver.find_element_by_xpath("//h5[text()='Combo Meal']").is_displayed() == True

#2:
def test_reset_password(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//*[@id='forgotId']").click()
    driver.find_element_by_xpath("//*[@id='inputForgotPassword']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//button[text()='Reset Password']").click()
    time.sleep(3)
    alert = driver.switch_to.alert
    msg = alert.text
    assert msg == "Check your inbox for further instructions"
    alert.dismiss()

#3:
def test_weather_jerusalem(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@id='location-name']").clear()
    driver.find_element_by_xpath("//input[@id='location-name']").send_keys("Jerusalem")
    driver.find_element_by_xpath("//button[text()='Search']").click()
    assert driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/p[2]/strong").is_displayed() == True

#4:
def test_weather_haifa(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@id='location-name']").clear()
    driver.find_element_by_xpath("//input[@id='location-name']").send_keys("Haifa")
    driver.find_element_by_xpath("//button[text()='Search']").click()
    assert driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/p[2]/strong").is_displayed() == True

#5:
def test_wrong_password(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("12345")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    time.sleep(3)
    alert2 = driver.switch_to.alert
    msg = alert2.text
    assert msg == "Failed to log in"
    alert2.dismiss()

#Login page error handling:
#1:
def test_login_with_no_email(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    time.sleep(3)
    alert2 = driver.switch_to.alert
    msg = alert2.text
    assert msg == "Failed to log in"
    alert2.dismiss()

#2:
def test_weather_for_not_real_location(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@id='location-name']").clear()
    driver.find_element_by_xpath("//input[@id='location-name']").send_keys("aaa")
    driver.find_element_by_xpath("//button[text()='Search']").click()
    assert driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/p[2]/strong").is_displayed() == True


#SignUp Page Functionality test:

#1:
def test_signup_with_first_and_last_name(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your first name']").send_keys("Yovell")
    driver.find_element_by_xpath("//input[@placeholder='Type your last name']").send_keys('Bennnn')
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel2a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    assert driver.find_element_by_xpath("//h5[text()='Combo Meal']").is_displayed() == True

#2:
def test_signup_without_first_and_last_name(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    assert driver.find_element_by_xpath("//h5[text()='Combo Meal']").is_displayed() == True

#3:
def test_signup_weather_rehovot(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/SignUp")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@id='location-name']").clear()
    driver.find_element_by_xpath("//input[@id='location-name']").send_keys("Rehovot")
    driver.find_element_by_xpath("//button[text()='Search']").click()
    assert driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/p[2]/strong").is_displayed() == True

#4:
def test_signup_with_first_name(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your first name']").send_keys("Yovell")
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    assert driver.find_element_by_xpath("//h5[text()='Combo Meal']").is_displayed() == True

#5:
def test_signup_with_last_name(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your last name']").send_keys('Bennnn')
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    assert driver.find_element_by_xpath("//h5[text()='Combo Meal']").is_displayed() == True

#SignUp Page Error Handling:
#1:
def test_signup_password_less_than_six_char(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your first name']").send_keys("Yovell")
    driver.find_element_by_xpath("//input[@placeholder='Type your last name']").send_keys('Bennnn')
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel3a2@bgmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("12345")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("12345")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    time.sleep(3)
    alert3 = driver.switch_to.alert
    msg = alert3.text
    assert msg == "Error: Password should be at least 6 characters"
    alert3.dismiss()

#2:
def test_sign_up_password_and_confirm_doesnt_match(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Type your first name']").send_keys("Yovell")
    driver.find_element_by_xpath("//input[@placeholder='Type your last name']").send_keys('Bennnn')
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel3a2@bgmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Create Password']").send_keys("123456")
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("12345")
    driver.find_element_by_xpath("//button[text()='Sign Up']").click()
    time.sleep(3)
    alert4 = driver.switch_to.alert
    msg = alert4.text
    assert msg == "password and confirm error"
    alert4.dismiss()

#Choose&Order Products Functionality test:
#1:
def test_order_2_combo_meal(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("2")
    driver.find_element_by_xpath("//button[text()='Send']").click()
    assert driver.find_element_by_xpath("//h2[text()='129.8']").is_displayed() == True

#2:
def test_order_2_prodcuts(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("//button[text()='Send']").click()
    assert driver.find_element_by_xpath("//h2[text()='107.8']").is_displayed() == True

#3:
def test_log_out(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Log out ']").click()
    time.sleep(3)
    assert driver.find_element_by_xpath("//button[text()='Sign In']").is_displayed() == True

#4:
def test_cancel_prodcuts(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/h5").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("//button[text()='Send']").click()
    assert driver.find_element_by_xpath("//h2[text()='64.9']").is_displayed() == True

#5:
def test_change_table_number(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("//input[@max='99']").clear()
    driver.find_element_by_xpath("//input[@max='99']").send_keys("2")
    driver.find_element_by_xpath("//button[text()='Send']").click()
    assert driver.find_element_by_xpath("//h3[text()='2']").is_displayed() == True

#Choose&Order Products error handling tests:
#1:
def test_3_combomeal(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("3")
    driver.find_element_by_xpath("//button[text()='Send']").click()
    alert5 = driver.switch_to.alert
    msg = alert5.text
    assert msg == "Invalid value in quantity"
    alert5.dismiss()

#2:
def test_delete_table_number(setup):
    driver = setup
    driver.get("https://svburger1.co.il/#/Signin")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("Yovel1a2b@gmail.com")
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys("123456")
    driver.find_element_by_xpath("//button[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@id='root']/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()=' Reserve ']").click()
    driver.find_element_by_xpath("//input[@max='99']").clear()
    driver.find_element_by_xpath("//button[text()='Send']").click()
    alert6 = driver.switch_to.alert
    msg = alert6.text
    assert msg == "You must enter table No."
    alert6.dismiss()



