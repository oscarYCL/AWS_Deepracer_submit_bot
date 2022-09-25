from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import login

driver = webdriver.Chrome(ChromeDriverManager().install()) # Chrome

def login2aws():
    driver.get("https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_ap-northeast-1_aac3b5bf05957230&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=CssrZOQSczYKjyiVZAV_qJYSVCBjWZcBi2Kum9raVlg&code_challenge_method=SHA-256")
    driver.find_element("xpath", '//*[@id="aws-signin-general-user-selection-iam"]').click()
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="resolving_input"]').send_keys(login.account_ID)
    driver.find_element("xpath", '//*[@id="next_button"]').click()
    driver.find_element("xpath", '//*[@id="username"]').send_keys(login.IAM)
    driver.find_element("xpath", '//*[@id="password"]').send_keys(login.Password)
    driver.find_element("xpath", '//*[@id="signin_button"]').click()
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="errorPage"]/p/a').click() #Error page

def submit():
    driver.get(login.League_url)
    time.sleep(10)
    driver.find_element("xpath", '//*[@id="app"]/div/div/div/div/div/main/div/div[2]/div/main/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div/button/span').click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.CLASS_NAME,"awsui_button-trigger_18eso_14emu_97").click()
    path = '//*[@title="{}"]'.format(login.model_name)
    driver.find_element(By.XPATH, path).click()
    driver.find_element("xpath", '//*[@id="app"]/div/div/div/div/div/main/div/div[2]/div/main/div[2]/div/div/div[4]/div/div/div/span/button').click()
    time.sleep (600)
    
login2aws()
while True:
    submit()
