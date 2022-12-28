from selenium import webdriver

# Set the path to the Chrome driver
driver_path = "C:\\path\\to\\chromedriver.exe"

# Initialize the Chrome driver
driver = webdriver.Chrome(driver_path)

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Find the username and password input elements
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

# Enter the login credentials
username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Find the login button and click it
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the login process to complete
driver.implicitly_wait(10)

# Navigate to the Instagram home page
driver.get("https://www.instagram.com/")

# Find the "New Post" button and click it
new_post_button = driver.find_element_by_xpath("//button[@type='button']/div[text()='New Post']")
new_post_button.click()

# Wait for the "Add Photo" button to appear
driver.implicitly_wait(10)

# Find the "Add Photo" button and click it
add_photo_button = driver.find_element_by_xpath("//button[@type='button']/div[text()='Add Photo']")
add_photo_button.click()

# Wait for the file input element to appear
driver.implicitly_wait(10)

# Find the file input element and enter the path to the photo
file_input = driver.find_element_by_name("fileInput")
file_input.send_keys("C:\\path\\to\\photo.jpg")

# Wait for the photo to be uploaded
driver.implicitly_wait(10)

# Find the caption input element and enter the caption
caption_input = driver.find_element_by_xpath("//textarea[@placeholder='Write a caption…']")
caption_input.send_keys("My Instagram post!")

# Find the "Share" button and click it
share_button = driver.find_element_by_xpath("//button[@type='submit']/div[text()='Share']")
share_button.click()

# Wait for the post to be shared
driver.implicitly_wait(10)

# Close the Chrome driver
driver.quit()
