const { chromium } = require('playwright');

const proxy = {
  server: 'http://HOST:PORT',
  username: 'USERNAME',
  password: 'PASSWORD'
};

(async () => {
  const browser = await chromium.launch({ proxy });

  try {
    const page = await browser.newPage();
    await page.goto('https://ipinfo.io/json');

    const result = await page.textContent('body');
    console.log(result);
  } finally {
    await browser.close();
  }
})();