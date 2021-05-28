from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://localhost:4200')

browser.implicitly_wait(3)

email_element = browser.find_element_by_css_selector("input[name = 'usermail']")
password_element = browser.find_element_by_css_selector("input[name = 'passcode']")
submit_btn_element = browser.find_element_by_css_selector("button[name = 'loginButton']")

time.sleep(3)

email_element.send_keys("hassan123@secp.gov.pk")
password_element.send_keys("abc123.")
submit_btn_element.click()

time.sleep(3)

unAuthorized_elem = browser.find_element_by_id('unAutherizedAlert')
print("\n" + unAuthorized_elem.text + "\n")

email_element.clear()
password_element.clear()

time.sleep(3)

email_element.send_keys("muhammad.hassan@secp.gov.pk")
password_element.send_keys("Hassan123.")

time.sleep(3)
submit_btn_element.click()

home_data = browser.find_element_by_css_selector("div [class = 'jumbotron-fluid'] p")

print("Data from home page: ")
print("\n" + home_data.text + "\n")

time.sleep(3)

navbar_element_help = browser.find_element_by_partial_link_text("Help")
navbar_element_help.click()

time.sleep(3)

navbar_element_profile = browser.find_element_by_partial_link_text("Profile")
navbar_element_profile.click()

time.sleep(4)

navbar_element_admin = browser.find_element_by_partial_link_text("Admin")
navbar_element_admin.click()

time.sleep(3)

admin_search_element = browser.find_elements_by_tag_name("input")
admin_search_element[0].send_keys("Muhammad Azim")

time.sleep(3)

admin_search_button = browser.find_element_by_css_selector("button[name = 'button']")
admin_search_button.click()

time.sleep(3)

# modify_rights_button = browser.find_elements_by_css_selector("button")
# modify_rights_button[2].click()
#
# time.sleep(2)

# select_rights_element = browser.find_element_by_css_selector("[class = 'input-group-addon']")
# select_rights_element[1].select()

navbar_element_logout = browser.find_element_by_partial_link_text("Log Out")
navbar_element_logout.click()

time.sleep(4)

browser.quit()
