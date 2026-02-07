



const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        executablePath: '/usr/bin/chromium-browser',
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--no-first-run',
            '--no-zygote',
            '--single-process',
            '--disable-extensions',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding'
        ]
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2.625 }); // Android mobile
    
    // Real Outlook signup 2026
    await page.goto('https://signup.live.com/', { waitUntil: 'networkidle' });
    
    // Fill form
    await page.waitForSelector('#liveTileSignUp', { timeout: 10000 });
    await page.click('#liveTileSignUp');
    
    await page.waitForSelector('input[name="FirstName"]');
    await page.type('input[name="FirstName"]', 'Test');
    await page.type('input[name="LastName"]', 'User');
    
    const username = `termux${Date.now() % 100000}`;
    await page.type('input[name="MemberName"]', username);
    await page.type('input[name="Password"]', `Tx${Math.random().toString().slice(-8)}P@ss!`);
    
    // Skip phone - use recovery email
    await page.type('input[data-id="RecoveryEmailInput"]', `recover${Date.now()}@gmail.com`);
    
    await page.click('input[value="Next"]');
    await page.waitForTimeout(5000);
    
    // Handle any CAPTCHA (manual first run)
    console.log('🔄 Check browser - solve CAPTCHA if shown');
    await page.waitForTimeout(30000); // Manual CAPTCHA solve time
    
    // Check success
    const success = await page.evaluate(() => {
        return !document.querySelector('[data-id="error"]') && 
               (location.href.includes('inbox') || location.href.includes('outlook'));
    });
    
    if (success) {
        require('fs').appendFileSync('✅_OUTLOOK.txt', `${username}@outlook.com:TxPass123!\n`);
        console.log('🎉 SUCCESS!');
    }
    
    await browser.close();
})();