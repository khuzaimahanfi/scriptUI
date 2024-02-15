from flask import Flask, render_template, request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

def execute_selenium_script():
    chrome_options = webdriver.ChromeOptions()
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://alnafi.com/auth/sign-in")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys("khuzaima.hanfi@alnafi.edu.pk")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input').send_keys("123456Bb")
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/button').click()
    time.sleep(10)
    driver.get("https://alnafi.com/hidden/course/test-course")
    time.sleep(5)

    # add to cart
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/button[2]').click()
    time.sleep(5)

    # go to checkout
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/div[2]/div[2]/button').click()
    time.sleep(5)

    # easy paisa
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/form/div[1]/div/div[2]/div/label[2]/div').click()
    time.sleep(2)

    # enter number
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/form/div[1]/div/div[2]/div/label[2]/div[2]/input').send_keys("0316")
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/form/div[2]/div/div[2]/button').click()
    time.sleep(70)

    element = driver.find_element(By.XPATH, '//*[@id="swal2-title"]')
    element_text = element.text
    hard_coded_text = 'Oops'

    if element_text == hard_coded_text:
        result_message = "Success! Payment Success."
    else:
        result_message = "Failure! Payment Failed."

    time.sleep(5)
    driver.quit()

    return result_message

@app.route('/')
def index():
    print("sdfsdf")
    return render_template('index.html')

@app.route('/execute_script', methods=['POST'])
def execute_script():
    result_message = execute_selenium_script()
    return result_message

if __name__ == '__main__':
    app.run(debug=True,port=8000)
