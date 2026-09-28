const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1680, height: 980 } });
  await p.goto('file://' + __dirname + '/concepts.html');
  await p.waitForTimeout(300);
  await p.screenshot({ path: __dirname + '/CivRebar_AI_3_pistes.png' });
  await b.close();
})();
