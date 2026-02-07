



#!/usr/bin/env python3
import requests
import random
import json
import time
from fake_useragent import UserAgent

ua = UserAgent()
session = requests.Session()
session.headers.update({'User-Agent': ua.random})

def create_outlook_account():
    proxies = {'http': 'http://your-proxy:port'}  # proxies.txt থেকে rotate
    
    # Step 1: Get signup token
    resp = session.get('https://signup.live.com/API/CreateAccount?lic=1', proxies=proxies)
    if resp.status_code != 200:
        return None
    
    data = resp.json()
    flowToken = data['flowToken']
    
    # Step 2: Personal info
    personal_data = {
        'FirstName': 'John', 'LastName': 'Doe',
        'BirthYear': '1990', 'BirthMonth': random.randint(1,12), 'BirthDay': random.randint(1,28),
        'DisplayName': 'John Doe'
    }
    
    resp = session.post('https://signup.live.com/API/PersonalDetails', json=personal_data, proxies=proxies)
    if 'error' in resp.text:
        return None
    
    # Step 3: Username/Password (hotmail bypass)
    username = f"termux{random.randint(10000,99999)}@hotmail.com"
    pw = "Pass123!@#Strong"
    
    account_data = {
        'MemberName': username.split('@')[0],
        'DomainName': 'hotmail.com',
        'Password': pw, 'RetypePassword': pw,
        'flowToken': flowToken
    }
    
    resp = session.post('https://signup.live.com/API/AccountCreate', json=account_data, proxies=proxies)
    
    if resp.status_code == 200 and 'success' in resp.text.lower():
        with open('accounts.txt', 'a') as f:
            f.write(f"{username}:{pw}\n")
        print(f"✅ {username}:{pw}")
        return username
    
    print("❌ Failed")
    return None

# Bulk
for i in range(20):
    create_outlook_account()
    time.sleep(random.randint(20,40))