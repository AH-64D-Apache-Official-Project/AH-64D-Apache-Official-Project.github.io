// Screenshot local HTML files with Playwright: node shoot.js jobs.json
// jobs: [{"html": path, "png": path, "width": n, "height": n, "transparent": bool}]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.width, height: j.height } });
    await page.goto('file://' + j.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(j.wait || 300);
    await page.screenshot({ path: j.png, omitBackground: !!j.transparent });
    await page.close();
  }
  await browser.close();
})();
