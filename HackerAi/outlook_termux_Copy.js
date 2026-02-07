// outlook_real.js - Termux + REAL flow
const axios = require('axios');
const fs = require('fs');

const session = axios.create({
    timeout: 45000,
    headers: {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors'
    }
});

// Skip phone verification - use existing recovery email pattern
async function createWithoutPhone() {
    try {
        console.log('🔄 Getting flowToken...');
        
        // Step 1: Get signup flow
        const flowReq = await session.get('https://signup.live.com/signup', {
            params: { 'wa': 'wsignin1.0', 'rup': 'https://account.microsoft.com/' }
        });
        
        const flowToken = flowReq.data.match(/"flowToken":"([^"]+)"/)?.[1];
        if (!flowToken) throw new Error('No flowToken');
        
        console.log('✅ Flow token OK');
        
        // Step 2: Create with recovery email (bypasses phone)
        const username = `tx${Date.now() % 100000}@outlook.com`;
        const password = `Tx${Math.floor(Math.random()*8999+1000)}P@ssw0rd!`;
        
        console.log(`📧 Creating: ${username}`);
        
        const createData = {
            flowToken,
            firstName: 'Test',
            lastName: 'User',
            username,
            password: { primary: password },
            recoveryEmail: `recover${Math.floor(Math.random()*999)}@gmail.com`,
            birthYear: 1990,
            birthMonth: 5,
            birthDay: 15
        };
        
        const createRes = await session.post('https://signup.live.com/API/AccountCreate', 
            createData, { headers: { 'Content-Type': 'application/json' } }
        );
        
        if (createRes.data.success || createRes.data.flowToken) {
            // Immediate login test
            const loginRes = await session.post('https://login.live.com/ppsecure/post.srf', 
                new URLSearchParams({
                    'loginfmt': username,
                    'passwd': password,
                    'wa': 'wsignin1.0'
                }), 
                { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
            );
            
            if (loginRes.data.includes('odc=') || !loginRes.data.includes('error')) {
                fs.appendFileSync('✅_WORKING_OUTLOOK.txt', `${username}:${password}\n`);
                console.log(`🎉 SUCCESS: ${username}`);
                return true;
            }
        }
        
        console.log('❌ Account verification failed');
        return false;
        
    } catch(error) {
        console.log(`💥 Error: ${error.response?.status} - ${error.message}`);
        return false;
    }
}

// Main loop
async function main() {
    console.log('🚀 Termux Outlook REAL Creator (Phone Bypass)\n');
    let success = 0;
    
    for(let i = 0; i < 10; i++) {  // Reduced for testing
        const ok = await createWithoutPhone();
        if (ok) success++;
        
        // Critical delay
        console.log(`⏳ Wait 90s... (${success} success)`);
        await new Promise(r => setTimeout(r, 90000));
    }
    
    console.log(`\n✅ Final: ${success}/10 accounts in WORKING_OUTLOOK.txt`);
}

main();