




const axios = require('axios');
const fs = require('fs');

async function createAccount() {
    const username = `node${Math.floor(Math.random()*90000)+10000}@hotmail.com`;
    const password = 'NodePass123!';
    
    try {
        // তোমার API call এখানে (এটা simplified, আসলে কাজ করবে না — নিচে ব্যাখ্যা আছে)
        let res = await axios.get('https://signup.live.com/API/CreateAccount?lic=1', {
            headers: {'User-Agent': 'Mozilla/5.0 (Linux; Android 11)'}
        });
        
        console.log(`✅ \( {username}: \){password}`);
        fs.appendFileSync('accounts.txt', `\( {username}: \){password}\n`);
    } catch(e) {
        console.log('❌ Fail:', e.message);
    }
}

// এই অংশটা চেঞ্জ করো
(async () => {
    for(let i = 0; i < 15; i++) {
        await createAccount();  // await দিয়ে কল করো যাতে একটা শেষ হলে পরেরটা শুরু হয়
        await new Promise(r => setTimeout(r, 30000));  // 30 সেকেন্ড delay
    }
    console.log('All done!');
})();