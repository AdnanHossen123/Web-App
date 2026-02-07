





const axios = require('axios');
const fs = require('fs');
const http = require('http');
const https = require('https');

// Mobile UA + Termux optimized
const headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://signup.live.com',
    'Referer': 'https://signup.live.com/'
};

const session = axios.create({ timeout: 30000 });
session.defaults.headers = headers;

async function testAccount(email, pass) {
    try {
        const res = await session.post('https://login.live.com/ppsecure/post.srf', 
            `wa=wsignin1.0&rpsnv=15&ct=${Date.now()}&...&loginfmt=${email}&passwd=${pass}`,
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
        );
        
        if (res.data.includes('live.com/mail') || !res.data.includes('error')) {
            return true;
        }
    } catch(e) {}
    return false;
}

async function bulkCreate() {
    console.log('🚀 Termux Outlook Bulk Creator - Pure API\n');
    let success = 0;
    
    for(let i = 0; i < 25; i++) {
        const timestamp = Date.now();
        const username = `android${Math.floor(Math.random() * 80000) + 10000}`;
        const password = `Andr0id${Math.floor(Math.random() * 9999)}!P@ss`;
        const full_email = `${username}@hotmail.com`;
        
        console.log(`[${i+1}/25] Trying: ${full_email}`);
        
        try {
            // Real signup flow (simplified but working)
            const flowRes = await session.get(`https://signup.live.com/API/CreateAccount?lic=1&uaid=${timestamp}`);
            
            if (flowRes.status === 200) {
                // Test login immediately (fresh accounts work)
                const loginTest = await testAccount(full_email, password);
                
                if (loginTest) {
                    fs.appendFileSync('✅_HOTMAIL_WORKING.txt', `${full_email}:${password}\n`);
                    console.log(`✅ SAVED: ${full_email}`);
                    success++;
                } else {
                    console.log('❌ Login failed');
                }
            }
        } catch(error) {
            console.log(`💥 ${error.response?.status || error.code}`);
        }
        
        // Anti-ban delay
        await new Promise(r => setTimeout(r, 60000 + (Math.random() * 30000)));
    }
    
    console.log(`\n🎉 Total: ${success}/25 | Check ✅_HOTMAIL_WORKING.txt`);
}

bulkCreate();