const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    proxy: {
      server: 'http://HOST:PORT',
      username: 'USERNAME',
      password: 'PASSWORD'
    }
  });

  try {
    const page = await browser.newPage();

    await page.goto('https://ipinfo.io/json');

    console.log(await page.textContent('body'));
  } finally {
    await browser.close();
  }
})();