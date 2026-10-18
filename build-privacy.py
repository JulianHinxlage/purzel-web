"""Wraps the Termly export (Privacy_Policy.html) in the site layout -> privacy.html.

Run again after re-exporting the policy from Termly:  python3 build-privacy.py
"""
from pathlib import Path

here = Path(__file__).resolve().parent
policy = (here / 'Privacy_Policy.html').read_text(encoding='utf-8')

page = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Privacy Policy · Purzel</title>
    <meta name="description" content="How Purzel handles your data." />
    <link rel="icon" href="favicon.ico" sizes="any" />
    <link rel="icon" type="image/png" href="favicon.png" />
    <link rel="apple-touch-icon" href="apple-touch-icon.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="wrap">
      <header class="site-header">
        <a class="brand" href="index.html"><img src="assets/icon.png" alt="" />Purzel</a>
        <nav>
          <a href="index.html#support">Support</a>
          <a href="privacy.html">Privacy</a>
        </nav>
      </header>
      <main class="doc policy">
{policy}
      </main>
    </div>
    <footer class="site-footer">
      <div class="wrap">
        <span>© 2026 Julian Rolf Hinxlage</span>
        <nav>
          <a href="privacy.html">Privacy Policy</a>
          <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Terms of Use</a>
          <a href="impressum.html">Impressum</a>
          <a href="mailto:hinxlage.solutions@gmail.com">Contact</a>
        </nav>
      </div>
    </footer>
  </body>
</html>
"""
(here / 'privacy.html').write_text(page, encoding='utf-8')
print('privacy.html written')
