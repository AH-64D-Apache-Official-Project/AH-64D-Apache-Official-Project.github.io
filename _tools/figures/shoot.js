// Screenshot local HTML files with Playwright: node shoot.js jobs.json
// jobs: [{"html": path, "png": path, "width": n, "height": n, "transparent": bool}]
// FM_CHROME_CHANNEL=chrome uses an installed Chrome instead of Playwright's own Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const { pathToFileURL } = require('url');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch({ channel: process.env.FM_CHROME_CHANNEL || undefined, args: ['--allow-file-access-from-files'] });
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.width, height: j.height } });
    await page.goto(pathToFileURL(j.html).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(j.wait || 300);
    await page.screenshot({ path: j.png, omitBackground: !!j.transparent });
    await page.close();
  }
  await browser.close();
})();
