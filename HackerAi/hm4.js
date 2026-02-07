





const axios = require('axios');
const fs = require('fs');

async function createAccount() {
    const username = `node${Math.floor(Math.random()*90000)+10000}@hotmail.com`;
    const password = 'NodePass123!';
    
    try {
        let res = await axios.get('https://signup.live.com/API/CreateAccount?lic=1', {
            headers: {'User-Agent': 'Mozilla/5.0 (Linux; Android 11)'}
        });
        
        // Simplified POST chain...
        console.log(`✅ ${username}:${password}`);
        fs.appendFileSync('accounts.txt', `${username}:${password}\n`);
    } catch(e) {
        console.log('❌ Fail');
    }
}

for(let i=0; i<15; i++) {
    createAccount();
    await new Promise(r=>setTimeout(r, 30000));
}