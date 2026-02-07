




#!/usr/bin/env python3
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, random, requests
import os

# Config - 2captcha API key (buy from 2captcha.com, ~$1/1000 CAPTCHAs)
CAPTCHA_API_KEY = "YOUR_2CAPTCHA_KEY_HERE"  # Change this!
PROXY_FILE = "proxies.txt"  # Residential proxies list
PROFILES_DIR = "./outlook_profiles"  # Save created accounts
os.makedirs(PROFILES_DIR, exist_ok=True)

def get_proxy():
    with open(PROXY_FILE, 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]
    return random.choice(proxies) if proxies else None

def solve_captcha(driver):
    # 2captcha for reCAPTCHA/hCaptcha
    sitekey = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
    url = driver.current_url
    
    # Submit to 2captcha
    resp = requests.post("http://2captcha.com/in.php", data={
        'key': CAPTCHA_API_KEY,
        'method': 'userrecaptcha',
        'googlekey': sitekey,
        'pageurl': url,
        'json': 1
    }).json()
    
    if resp['status'] != 1:
        print(f"CAPTCHA submit fail: {resp}")
        return False
    
    captcha_id = resp['request']
    for _ in range(30):  # Wait up to 5min
        time.sleep(10)
        result = requests.get(f"http://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={captcha_id}&json=1").json()
        if result['status'] == 1:
            driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{result['request']}';")
            return True
    return False

def create_account(username_base="testuser", password="StrongPass123!"):
    proxy = get_proxy()
    options = uc.ChromeOptions()
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    driver = uc.Chrome(options=options, version_main=120)  # Match your Chromium
    
    try:
        driver.get("https://outlook.live.com/owa/?nlp=1&signup=1")
        wait = WebDriverWait(driver, 20)
        
        # Fill first name, last name, birthdate (random to evade)
        wait.until(EC.presence_of_element_located((By.NAME, "FirstName"))).send_keys("John")
        driver.find_element(By.NAME, "LastName").send_keys("Doe")
        driver.find_element(By.ID, "BirthMonth").send_keys(str(random.randint(1,12)))
        driver.find_element(By.ID, "BirthDay").send_keys(str(random.randint(1,28)))
        driver.find_element(By.ID, "BirthYear").send_keys("1990")
        
        # Username (hotmail.com)
        username = f"{username_base}{random.randint(1000,9999)}@hotmail.com"
        wait.until(EC.element_to_be_clickable((By.NAME, "MemberName"))).send_keys(username.split('@')[0])
        driver.find_element(By.ID, "LiveDomainId").send_keys("hotmail.com")
        
        driver.find_element(By.ID, "iSignupAction").click()
        
        # Password
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys(password)
        driver.find_element(By.NAME, "RetypePassword").send_keys(password)
        
        # CAPTCHA if appears
        if "recaptcha" in driver.page_source.lower():
            if not solve_captcha(driver):
                print("CAPTCHA solve failed!")
                return None
        
        driver.find_element(By.ID, "iSignupAction").click()
        
        # Skip phone (sometimes skips if proxy/resi IP clean)
        time.sleep(5)
        if "verify" in driver.current_url.lower() or "phone" in driver.page_source.lower():
            print("Phone verification hit - trying skip/add alt email")
            # Alt email skip (if prompted)
            try:
                driver.find_element(By.ID, "use-email").click()  # Fake alt email option
            except:
                print("Phone block - bad proxy/session")
                return None
        
        # Success check
        if "inbox" in driver.current_url or "outlook.live.com/mail":
            profile_file = f"{PROFILES_DIR}/{username}.txt"
            with open(profile_file, 'w') as f:
                f.write(f"Email: {username}\nPassword: {password}\nCreated: {time.ctime()}\nProxy: {proxy}")
            print(f"✅ SUCCESS: {username} | Saved to {profile_file}")
            return username
        
    except TimeoutException:
        print("Timeout - page slow/blocked")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
    return None

# Bulk run
if __name__ == "__main__":
    success_count = 0
    for i in range(10):  # Create 10 accounts
        print(f"\n--- Attempt {i+1}/10 ---")
        if create_account(f"hacker{random.randint(100,999)}"):
            success_count += 1
        time.sleep(random.randint(30,60))  # Rate limit evade
    print(f"\nTotal success: {success_count}/10")