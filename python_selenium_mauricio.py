import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# Add WebDriver to PATH
os.environ['PATH'] += r"C:/SeleniumDrivers"
# Fix for Selenium Browser that Closes Automatically & Immediately After Test
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://demo.evershop.io/")
driver.implicitly_wait(30)

# find the element of the login icon with the href="/account/login" attribute
login_link = driver.find_element(By.XPATH, '//a[@href="/account/login"]')
# click on the login icon
login_link.click()

# find the "create an account" interactive text
create_account = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/a')
# click on the "create an account" interactive text
create_account.click()

# find the name input element
name_input = driver.find_element(By.NAME, "full_name")
# fill the name input element with the provided keys
name_input.send_keys("Mauricio")
# find the email input element
email_input = driver.find_element(By.NAME, "email")
# fill the email input element with the provided keys
email_input.send_keys("mauricio123@gmail.com")
# find the password input element
password_input = driver.find_element(By.NAME, "password")
# fill the password input element with the provided keys
password_input.send_keys("selenium123")

# find the "Login" interactive text
login_account_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/span/a')
# click on the "Login" interactive text
login_account_button.click()

# find the email input element
email_input2 = driver.find_element(By.NAME, "email")
# fill the email input element with the provided keys
email_input2.send_keys("mauricio123@gmail.com")
# find the password input element
password_input2 = driver.find_element(By.NAME, "password")
# fill the password input element with the provided keys
password_input2.send_keys("selenium123")

# find the "Signin" button
signin_account_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[3]/button/span')
# click on the "Signin" button
signin_account_button.click()
time.sleep(1)

# Go to men category
men_category_link = driver.find_element(By.XPATH, '//a[@href="/category/men"]')
men_category_link.click()
time.sleep(1)
# Find a shoe
item1 = driver.find_element(By.XPATH, "(//span[contains(text(),'Nmd_r1 shoes')])[1]")
item1.click()
# Find quantity attribute and input a value
quantity_item1 = driver.find_element(By.NAME, 'qty')
quantity_item1.clear()
quantity_item1.send_keys("4")
# Find shoe size and select one
add_size = driver.find_element(By.XPATH, "//a[normalize-space()='X']")
add_size.click()
# Find shoe color and select one
aDD_color = driver.find_element(By.XPATH, "//a[normalize-space()='Black']")
aDD_color.click()
time.sleep(1)
# Find add to cart button and click on it
add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="productForm"]/div/div/div[2]/button/span')
add_to_cart_button.click()
time.sleep(1)

# Go to KIDS category
kids_category_link = driver.find_element(By.XPATH, '//a[@href="/category/kids"]')
kids_category_link.click()
time.sleep(1)
# Find a shoe
item2 = driver.find_element(By.XPATH, "//span[normalize-space()='Continental 80 shoes']")
item2.click()
# Find quantity attribute and input a value
quantity_item2 = driver.find_element(By.NAME, 'qty')
quantity_item2.clear()
quantity_item2.send_keys("2")
# Find shoe size and select one
add_size2 = driver.find_element(By.XPATH, "//a[normalize-space()='L']")
add_size2.click()
# Find shoe color and select one
aDD_color2 = driver.find_element(By.XPATH, "//a[normalize-space()='White']")
aDD_color2.click()
time.sleep(1)
# Find add to cart button and click on it
add_to_cart_button2 = driver.find_element(By.XPATH, '//*[@id="productForm"]/div/div/div[2]/button/span')
add_to_cart_button2.click()
time.sleep(1)


# Go to women category
women_category_link = driver.find_element(By.XPATH, '//a[@href="/category/women"]')
women_category_link.click()
time.sleep(1)
# Find a shoe
item3 = driver.find_element(By.XPATH, "//span[normalize-space()='Alphaedge 4d reflective shoes R']")
item3.click()
# Find quantity attribute and input a value
quantity_item3 = driver.find_element(By.NAME, 'qty')
quantity_item3.clear()
quantity_item3.send_keys("5")
# Find shoe size and select one
add_size3 = driver.find_element(By.XPATH, "//a[normalize-space()='M']")
add_size3.click()
# Find shoe color and select one
aDD_color3 = driver.find_element(By.XPATH, "//a[normalize-space()='White']")
aDD_color3.click()
time.sleep(1)
# Find add to cart button and click on it
add_to_cart_button3 = driver.find_element(By.XPATH, '//*[@id="productForm"]/div/div/div[2]/button/span')
add_to_cart_button3.click()
time.sleep(1)

# go to FIRST page
home_button = driver.find_element(By.CLASS_NAME, "logo-icon")
home_button.click()

# go to cart
go_to_cart_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/a/span')
go_to_cart_button.click()

# click on checkout button
checkout_button = driver.find_element(By.XPATH, "//a[@class='button primary']")
checkout_button.click()


# find the email input element
full_name_2 = driver.find_element(By.NAME, "address[full_name]")
full_name_2.send_keys("Mauricio Oscar Nuñez Melgarejo")

# find telephone input element
telephone = driver.find_element(By.NAME, "address[telephone]")
telephone.send_keys("(01)-4069422")

# find address input element
address1 = driver.find_element(By.NAME, "address[address_1]")
address1.send_keys("Avenida Felipe Santiago Salaverry, 398, Urb. Ind. El Pino")

# find city input element
city = driver.find_element(By.NAME, "address[city]")
city.send_keys("San Luis")

# find postcode input element
postcode = driver.find_element(By.NAME, "address[postcode]")
postcode.send_keys("15089")

# find country input element
country = driver.find_element(By.ID, "address[country]")
option_country = Select(country)
option_country.select_by_value("CN")

# find province input element
province = driver.find_element(By.ID, "address[province]")
option_province = Select(province)
option_province.select_by_value("CN-34")

# find shipping method element
shipping_method_button = driver.find_element(By.XPATH, '//*[@id="checkoutShippingAddressForm"]/div[1]/div[6]/div/div/div/div[1]/label/span[1]')
shipping_method_button.click()

# find payment continue button
payment_continue_button = driver.find_element(By.XPATH, '//*[@id="checkoutShippingAddressForm"]/div[2]/button/span')
payment_continue_button.click()

time.sleep(1)

# find payment method SVG click-able element
element = driver.find_element(By.XPATH, "//*[local-name()='svg' and @class='feather feather-circle']")
element.click()

time.sleep(3)

#After this, i couldn't find a way to only ENTER intengers numbers to the card number field, i tried many way from a
# loop to using ActionsCHAINS but nothing worked. I hope you could send me the correct soulution of this part.

