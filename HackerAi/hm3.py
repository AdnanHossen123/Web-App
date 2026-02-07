




from playwright.sync_api import sync_playwright
import random, time

def create_account():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
            proxy={'server': 'http://proxy:port'}  # Optional
        )
        page = context.new_page()
        
        page.goto('https://outlook.live.com/owa/?nlp=1&signup=1')
        
        # Fill form fast
        page.fill('input[name="FirstName"]', 'Ali')
        page.fill('input[name="LastName"]', f'Doe{random.randint(100,999)}')
        page.select_option('#BirthMonth', str(random.randint(1,12)))
        page.select_option('#BirthDay', str(random.randint(1,28)))
        page.fill('#BirthYear', '1995')
        
        username = f"tx{random.randint(10000,99999)}@hotmail.com"
        page.fill('input[name="MemberName"]', username.split('@')[0])
        page.select_option('#LiveDomainId', 'hotmail.com')
        
        page.click('#iSignupAction')
        time.sleep(3)
        
        page.fill('input[name="Password"]', 'Passw0rd!123')
        page.fill('input[name="RetypePassword"]', 'Passw0rd!123')
        page.click('#iSignupAction')
        
        # Phone skip (if clean IP)
        if page.is_visible('text=Use a different email'):
            page.click('text=Use a different email')
        
        if 'inbox' in page.url:
            print(f"✅ SUCCESS: {username}")
            return username
        
        browser.close()
    return None

for _ in range(10):
    create_account()
    time.sleep(30)