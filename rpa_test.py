from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/add?num1=10&num2=5")
assert "15" in driver.page_source
driver.quit()
