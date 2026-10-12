# Setup (about 15 minutes, all free)

1. Supabase: create a free project, open SQL Editor, paste and run `supabase.sql`.
   Then Settings > API: copy the Project URL and the `anon public` key into `src/config.js`.
2. Edit the top of `build.py`: SITE_URL, EMAIL (and later ADSENSE).
3. Build: `python3 build.py`  -> the finished site is in `dist/`.
4. Deploy `dist/` on Cloudflare Pages or Netlify (drag and drop or connect GitHub).
5. Buy a custom domain (AdSense usually rejects free subdomains) and point it to the site.
6. Approve stories: Supabase > Table Editor > stories > tick `approved`.

## Before applying to AdSense
- Publish 15-25 original articles (not copied, not AI-pasted without editing). Add them in build.py with `page(...)`.
- Make sure Privacy Policy, About, Contact and Medical Disclaimer links work.
- Add real contact email and a few approved community stories.
- Apply at adsense.google.com, add your site, paste the verification code (set ADSENSE in build.py and rebuild).
