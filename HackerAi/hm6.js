



const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
    const browser = await chromium.launch({ 
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    for(let i = 0; i < 10; i++) {
        console.log(`\n--- Account ${i+1}/10 ---`);
        const context = await browser.newContext({
            userAgent: 'Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36',
            viewport: { width: 412, height: 915 }  // Mobile evade
        });
        
        const page = await context.newPage();
        
        try {
            await page.goto('https://outlook.live.com/owa/?nlp=1&signup=1&signupwp=0');
            await page.waitForLoadState('networkidle');
            
            // Fill form
            await page.fill('input[name="FirstName"]', 'Rahi');
            await page.fill('input[name="LastName"]', `Test${Math.floor(Math.random()*999)}`);
            await page.selectOption('#BirthMonth', `${Math.floor(Math.random()*12)+1}`);
            await page.selectOption('#BirthDay', `${Math.floor(Math.random()*28)+1}`);
            await page.fill('#BirthYear', '1995');
            
            const username = `tx${Math.floor(Math.random()*90000)+10000}`;
            await page.fill('input[name="MemberName"]', username);
            await page.selectOption('#LiveDomainId option[value="hotmail.com"]', 'hotmail.com');
            
            await page.click('#iSignupAction');
            await page.waitForTimeout(3000);
            
            await page.fill('input[name="Password"]', 'RahulPass123!');
            await page.fill('input[name="RetypePassword"]', 'RahulPass123!');
            
            await page.click('#iSignupAction');
            await page.waitForTimeout(5000);
            
            // Success check
            if (page.url().includes('inbox') || page.url().includes('outlook.live.com/mail')) {
                fs.appendFileSync('valid_accounts.txt', `${username}@hotmail.com:RahulPass123!\n`);
                console.log(`✅ VALID: ${username}@hotmail.com`);
            } else {
                console.log('❌ No inbox redirect');
            }
            
        } catch(e) {
            console.log('💥 Error:', e.message);
        }
        
        await context.close();
        await new Promise(r => setTimeout(r, 60000)); // 1min delay
    }
    
    await browser.close();
})();