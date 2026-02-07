#!/usr/bin/env python3
"""
Fixed Facebook Creator for TermUX - No undetected-chromedriver needed
"""

import os
import json
import time
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from faker import Faker

fake = Faker()

class FacebookCreator:
    def __init__(self, proxy=None):
        self.proxy = proxy
        self.profiles = self.load_profiles()
        self.successful_accounts = []
    
    def load_profiles(self):
        profiles = []
        for i in range(5):  # 5 accounts (less spam detection)
            profiles.append({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': f"fbtest{random.randint(10000,99999)}@10minutemail.com",
                'password': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=12)),
                'day': str(random.randint(1,28)),
                'month': str(random.randint(1,12)),
                'year': str(random.randint(1990,2000))
            })
        return profiles
    
    def setup_driver(self):
        """Termux Chrome setup - Fixed for Android"""
        options = Options()
        
        # Essential Termux Chrome flags
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-background-timer-throttling')
        options.add_argument('--disable-backgrounding-occluded-windows')
        options.add_argument('--disable-renderer-backgrounding')
        options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36')
        options.add_argument('--window-size=360,760')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Proxy
        if self.proxy:
            options.add_argument(f'--proxy-server={self.proxy}')
        
        # Termux Chrome path
        chrome_options = options.to_capabilities()
        chrome_options['goog:chromeOptions'] = options.to_capabilities()['goog:chromeOptions']
        
        # Find Chrome binary in Termux
        chromedriver_path = "/data/data/com.termux/files/usr/bin/chromedriver"
        service = Service(chromedriver_path)
        
        driver = webdriver.Chrome(service=service, options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    
    def human_delay(self, min_sec=2, max_sec=5):
        time.sleep(random.uniform(min_sec, max_sec))
    
    def create_account(self, profile):
        print(f"🔄 Creating: {profile['first_name']} {profile['last_name']}")
        
        driver = None
        try:
            driver = self.setup_driver()
            driver.get("https://m.facebook.com/r.php")  # Mobile version
            self.human_delay(4, 7)
            
            # First name
            first_input = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.NAME, "firstname"))
            )
            first_input.clear()
            first_input.send_keys(profile['first_name'])
            self.human_delay(1, 3)
            
            # Last name
            last_input = driver.find_element(By.NAME, "lastname")
            last_input.clear()
            last_input.send_keys(profile['last_name'])
            self.human_delay(1, 2)
            
            # Email
            email_input = driver.find_element(By.NAME, "reg_email__")
            email_input.clear()
            email_input.send_keys(profile['email'])
            self.human_delay(1, 2)
            
            # Confirm email
            confirm_email = driver.find_element(By.NAME, "reg_email_confirmation__")
            confirm_email.clear()
            confirm_email.send_keys(profile['email'])
            self.human_delay(1, 2)
            
            # Password
            pass_input = driver.find_element(By.NAME, "reg_passwd__")
            pass_input.send_keys(profile['password'])
            self.human_delay(1, 2)
            
            # Birthday
            day_select = driver.find_element(By.NAME, "birthday_day")
            day_select.send_keys(profile['day'])
            
            month_select = driver.find_element(By.NAME, "birthday_month")
            month_select.send_keys(profile['month'])
            
            year_select = driver.find_element(By.NAME, "birthday_year")
            year_select.send_keys(profile['year'])
            self.human_delay(2, 3)
            
            # Gender - Male/Female random
            genders = driver.find_elements(By.CSS_SELECTOR, "input[name='sex']")
            if genders:
                random.choice(genders).click()
                self.human_delay(1, 2)
            
            # Submit
            submit_btn = driver.find_element(By.NAME, "websubmit")
            driver.execute_script("arguments[0].click();", submit_btn)
            
            self.human_delay(8, 12)
            
            current_url = driver.current_url
            if "facebook.com" in current_url and "checkpoint" not in current_url.lower():
                account = {
                    'email': profile['email'],
                    'password': profile['password'],
                    'name': f"{profile['first_name']} {profile['last_name']}"
                }
                self.successful_accounts.append(account)
                print(f"✅ SUCCESS: {profile['email']} | Pass: {profile['password']}")
                return True
            else:
                print("❌ Failed - probably captcha/checkpoint")
                
        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}")
        
        finally:
            if driver:
                driver.quit()
        
        return False
    
    def run(self):
        print("🚀 Facebook Account Creator Started!")
        print(f"📱 Mobile mode | Mobile Facebook URL")
        
        for i, profile in enumerate(self.profiles, 1):
            print(f"\n{'='*50}")
            print(f"Account {i}/{len(self.profiles)}")
            print(f"{'='*50}")
            
            success = self.create_account(profile)
            
            if i < len(self.profiles):
                wait_time = random.randint(600, 900)  # 10-15 mins
                print(f"⏳ Waiting {wait_time//60} mins before next...")
                time.sleep(wait_time)
        
        self.save_results()
    
    def save_results(self):
        if self.successful_accounts:
            filename = f"fb_accounts_success_{int(time.time())}.txt"
            with open(filename, 'w') as f:
                f.write("Facebook Accounts Created:\n\n")
                for acc in self.successful_accounts:
                    f.write(f"Email: {acc['email']}\n")
                    f.write(f"Pass:  {acc['password']}\n")
                    f.write(f"Name:  {acc['name']}\n\n")
            print(f"\n💾 Saved {len(self.successful_accounts)} accounts -> {filename}")
        else:
            print("😞 No successful accounts")

if __name__ == "__main__":
    creator = FacebookCreator()
    creator.run()