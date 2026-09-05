import os
import glob
import re

html_files = glob.glob('c:/Users/Freak/Desktop/Origins/*.html')

socials_html = """  <div class="fs" style="display:flex;gap:20px;flex-wrap:wrap;justify-content:center;margin: 10px 0;">
    <a href="https://x.com/originssport?s=21&amp;t=obBPKKkXGFiuTGdN5IV35A" target="_blank" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">X</a>
    <a href="https://www.instagram.com/origins.esport.pro/" target="_blank" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">INSTAGRAM</a>
    <a href="https://www.tiktok.com/@origins.esport?_r=1&amp;_t=ZN-94lWSR8TOQo" target="_blank" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">TIKTOK</a>
    <a href="https://www.twitch.tv/originsesport_" target="_blank" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">TWITCH</a>
    <a href="https://discord.gg/4xBKUCCpfC" target="_blank" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">DISCORD</a>
    <a href="mailto:origins.esport.pro@gmail.com" class="ht" style="font-family:var(--fm);font-size:.58rem;color:var(--mt);text-decoration:none;letter-spacing:2px;transition:color .3s" onmouseover="this.style.color='var(--c)'" onmouseout="this.style.color='var(--mt)'">CONTACT</a>
  </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'https://discord.gg/4xBKUCCpfC' in content:
        continue
        
    # Inject it before <div class="fc">
    new_content = re.sub(
        r'(\s*<div class="fc">.*?</div>)', 
        '\n' + socials_html + r'\1', 
        content
    )
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')

print('Script finished.')
