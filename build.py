import os, shutil, datetime

SITE_NAME = "Lighter Together"
SITE_URL = "https://YOUR-DOMAIN.com"      # change after buying your domain
EMAIL = "contact@YOUR-DOMAIN.com"          # change to your real email
ADSENSE = ""                               # e.g. ca-pub-1234567890123456 (leave empty until approved)
TODAY = datetime.date.today().isoformat()

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "dist")
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
for f in ("style.css", "app.js", "config.js"):
    shutil.copy(os.path.join(SRC, f), OUT)

ADSCRIPT = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s" crossorigin="anonymous"></script>' % ADSENSE) if ADSENSE else ""

def ad():
    if not ADSENSE:
        return '<div class="ad"><!-- AdSense unit goes here after approval --></div>'
    return ('<div class="ad"><ins class="adsbygoogle" style="display:block" data-ad-client="%s" data-ad-slot="YOUR-SLOT-ID" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div>' % ADSENSE)

PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="stylesheet" href="style.css">
{adscript}
</head><body>
<header class="site"><div class="wrap">
<a class="logo" href="index.html">{site}</a>
<nav><a href="index.html">Home</a><a href="how-to-treat-severe-obesity.html">Guide</a><a href="community.html">Community</a><a href="share-your-story.html">Share</a><a href="ask.html">Ask</a><a href="about.html">About</a></nav>
</div></header>
{body}
<footer><div class="wrap">
<p><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy-policy.html">Privacy Policy</a><a href="terms.html">Terms</a><a href="medical-disclaimer.html">Medical Disclaimer</a></p>
<p>&copy; {year} {site}. Information on this site is for education only and is not medical advice. Always consult a qualified healthcare professional.</p>
</div></footer>
<script src="config.js"></script><script src="app.js"></script><script src="community.js"></script>
</body></html>"""

pages = []
def page(fn, title, desc, body):
    html = PAGE.format(title=title, desc=desc, url=SITE_URL + "/" + fn, body=body, site=SITE_NAME,
                       year=datetime.date.today().year, adscript=ADSCRIPT)
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    pages.append(fn)

DISC = '<div class="note"><strong>Medical note:</strong> This content is educational and does not replace advice from your doctor. Severe obesity is a medical condition that should be managed with a healthcare professional.</div>'

# ---------------- HOME ----------------
page("index.html", "Lighter Together - Severe Obesity Treatment Guide & Real Community Stories",
     "Evidence-based guidance on treating severe obesity, plus a supportive community where members share real weight loss journeys.",
f"""<section class="hero"><div class="wrap">
<h1>Real help for severe obesity. Real stories from people on the same road.</h1>
<p>Clear, evidence-based guidance on treatment options, and a community where members share what actually worked for them.</p>
<a class="btn" href="how-to-treat-severe-obesity.html">Read the guide</a>
<a class="btn" style="margin-left:8px;background:#0b4f4a;color:#fff" href="share-your-story.html">Share your story</a>
</div></section>
<main><div class="wrap">
{DISC}
<div class="grid">
<div class="card"><h3>Treatment guide</h3><p>Medical evaluation, nutrition, activity, medication and surgery explained in plain language.</p><a href="how-to-treat-severe-obesity.html">Read more &rarr;</a></div>
<div class="card"><h3>Community stories</h3><p>Read journeys from members who are lowering their weight, and learn from their wins and setbacks.</p><a href="community.html">Browse stories &rarr;</a></div>
<div class="card"><h3>Share your journey</h3><p>Your experience can encourage someone who is just starting. Stories are reviewed before publishing.</p><a href="share-your-story.html">Submit a story &rarr;</a></div>
</div>
{ad()}
<h2>Why this site exists</h2>
<p>Severe obesity (generally a BMI of 40 or more, or 35 or more with related health conditions) is complex. It is influenced by genetics, hormones, sleep, stress, environment and medical conditions, not just willpower. People do better with accurate information, medical support and a community that does not judge.</p>
</div></main>""")

# ---------------- PILLAR ARTICLE ----------------
page("how-to-treat-severe-obesity.html", "How to Treat Severe Obesity: A Practical, Evidence-Based Guide",
     "Learn how severe obesity is treated: medical evaluation, nutrition, physical activity, medications, bariatric surgery and long-term support.",
f"""<main><div class="wrap"><article>
<h1>How to Treat Severe Obesity: A Practical, Evidence-Based Guide</h1>
<p class="meta">Updated {TODAY} &middot; Reading time about 6 minutes</p>
{DISC}
<p>Severe obesity is a chronic medical condition, and it can be treated. The most successful plans combine several approaches and are adjusted over time with a healthcare team. This guide explains the main options so you can have a more informed conversation with your doctor.</p>

<h2>1. What counts as severe obesity?</h2>
<p>Doctors usually use body mass index (BMI). A BMI of 40 or higher is called class 3 (severe) obesity. A BMI of 35 or higher together with conditions such as type 2 diabetes, high blood pressure or sleep apnea is often treated in a similar way. BMI is only a screening tool, so your doctor will also look at waist size, blood tests and overall health.</p>

<h2>2. Start with a full medical evaluation</h2>
<p>Before changing your routine, book a checkup. A good evaluation looks for thyroid problems, insulin resistance, sleep apnea, depression, medication side effects and other factors that make weight loss harder. Treating these can make everything else easier.</p>
{ad()}
<h2>3. Set realistic goals</h2>
<p>Losing 5 to 10 percent of your starting weight already improves blood sugar, blood pressure and joint pain for many people. Bigger goals can come later. Slow, steady progress is easier to maintain than rapid loss.</p>

<h2>4. Nutrition that you can keep up</h2>
<ul>
<li><strong>Build meals around protein and fiber.</strong> Eggs, fish, poultry, legumes, vegetables and whole grains keep you full for longer.</li>
<li><strong>Reduce ultra-processed foods and sugary drinks.</strong> Liquid calories are one of the easiest places to cut.</li>
<li><strong>Plan, do not punish.</strong> Regular meals, prepared snacks and a simple shopping list prevent impulsive choices.</li>
<li><strong>Avoid crash diets.</strong> Extreme restriction often leads to rebound weight gain. A registered dietitian can create a plan that fits your culture and budget.</li>
</ul>

<h2>5. Move in a way your body can handle</h2>
<p>With severe obesity, joints and breathing can limit exercise, so begin gently. Short walks, swimming, water aerobics or cycling on a stationary bike are kind to the joints. Aim to build gradually toward about 150 minutes of moderate activity per week, and add light strength training twice a week when your doctor agrees.</p>

<h2>6. Sleep, stress and habits</h2>
<p>Poor sleep and chronic stress raise appetite hormones and cravings. Aim for regular sleep, and treat sleep apnea if you have it. Tracking food, steps or mood in a notebook helps you notice patterns without judgment. Behavioral therapy or counseling has good evidence for helping people change long-standing habits.</p>
{ad()}
<h2>7. Prescription medication</h2>
<p>For some adults, doctors prescribe anti-obesity medications alongside lifestyle changes. Newer medicines that act on gut hormones (the GLP-1 class, for example) have produced significant weight loss in clinical trials, but they are not suitable for everyone, can cause side effects, and must be prescribed and monitored by a physician. Never buy these medicines from unverified sellers.</p>

<h2>8. Bariatric (weight-loss) surgery</h2>
<p>Procedures such as sleeve gastrectomy and gastric bypass are among the most effective long-term treatments for severe obesity and can improve or resolve type 2 diabetes. They are major operations that require careful screening, lifelong vitamin supplementation and permanent changes to eating habits. Ask your doctor whether you meet the criteria and request a referral to a specialist program.</p>

<h2>9. Build a support system</h2>
<p>People who have encouragement, whether from family, a clinic, or an online community, tend to stay on track longer. Reading how others handled plateaus, cravings and setbacks can make your own path feel less lonely. Visit our <a href="community.html">community stories</a> to see real experiences, and consider <a href="share-your-story.html">sharing yours</a>.</p>

<h2>10. Maintenance is the real goal</h2>
<p>Weight regain is common, which is why long-term follow-up matters. Keep your weekly routines, weigh in regularly, and contact your care team early if weight starts to climb again. Needing ongoing support is normal for a chronic condition and is not a failure.</p>

<h2>When to seek urgent care</h2>
<p>Seek medical help right away if you have chest pain, severe shortness of breath, fainting, or signs of an eating disorder. Do not start extreme diets or unregulated supplements without medical advice.</p>
<p class="meta">This article is a general overview and is not a substitute for personal medical advice.</p>
</article></div></main>""")

# ---------------- COMMUNITY ----------------
page("community.html", "Community Weight Loss Stories | Lighter Together",
     "Read real experiences from members reducing obesity: what worked, what was hard, and what they learned.",
f"""<main><div class="wrap">
<h1>Community Stories</h1>
<p>Real experiences from members working on their health. Every story is reviewed before it appears. These are personal experiences, not medical advice.</p>
<p><a class="btn alt" href="share-your-story.html">Share your story</a></p>
{ad()}
<div id="stories"><p class="meta">Loading stories...</p></div>
</div></main>""")

page("share-your-story.html", "Share Your Weight Loss Story | Lighter Together",
     "Share your journey with obesity and weight loss to inspire others. Stories are reviewed before publishing.",
"""<main><div class="wrap"><article>
<h1>Share Your Story</h1>
<p>Your experience can help someone take their first step. Please use a nickname, avoid personal contact details, and do not recommend specific medicines or doses. Stories are reviewed and may be edited or declined.</p>
<form id="storyForm">
<label for="nickname">Nickname</label><input id="nickname" name="nickname" required minlength="2" maxlength="40">
<label for="title">Story title</label><input id="title" name="title" required minlength="5" maxlength="120" placeholder="e.g. How walking 20 minutes a day changed my year">
<label for="kg_lost">Weight lost in kg (optional)</label><input id="kg_lost" name="kg_lost" type="number" min="0" max="399" step="0.1">
<label for="months">Time in months (optional)</label><input id="months" name="months" type="number" min="0" max="239">
<label for="story">Your story</label><textarea id="story" name="story" required minlength="80" maxlength="4000" placeholder="What did you change? What was hardest? What would you tell a beginner?"></textarea>
<input type="text" name="website" tabindex="-1" autocomplete="off" style="display:none">
<p class="meta">By submitting you agree to our <a href="terms.html">Terms</a> and <a href="privacy-policy.html">Privacy Policy</a>.</p>
<button class="btn alt" type="submit">Submit story</button>
<div id="formMsg" class="msg"></div>
</form>
</article></div></main>""")

# ---------------- LEGAL / TRUST PAGES ----------------
page("about.html", "About Us | Lighter Together", "Who we are and why we built Lighter Together.",
f"""<main><div class="wrap"><article>
<h1>About {SITE_NAME}</h1>
<p>{SITE_NAME} is an educational website and community for people living with severe obesity and their families. Our goal is to explain treatment options clearly and to give members a safe, respectful place to share real experiences.</p>
<h2>Our approach</h2>
<p>Our articles are written to summarize widely accepted medical guidance and are reviewed for clarity. We do not promote miracle cures, extreme diets or unverified supplements. Community stories are personal and are moderated before publication.</p>
<h2>Important</h2>
<p>We are not a medical provider. Nothing here is a diagnosis or treatment plan. Please speak with a qualified healthcare professional about your own situation.</p>
<p>Questions? <a href="contact.html">Contact us</a>.</p>
</article></div></main>""")

page("contact.html", "Contact Us | Lighter Together", "Get in touch with the Lighter Together team.",
f"""<main><div class="wrap"><article>
<h1>Contact Us</h1>
<p>For questions, corrections, story removal requests or partnership inquiries, email us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>We aim to reply within a few business days. We cannot give personal medical advice. If you have a medical emergency, contact your local emergency number.</p>
</article></div></main>""")

page("privacy-policy.html", "Privacy Policy | Lighter Together", "How Lighter Together collects, uses and protects information.",
f"""<main><div class="wrap"><article>
<h1>Privacy Policy</h1>
<p class="meta">Last updated: {TODAY}</p>
<h2>Information we collect</h2>
<p>When you submit a story we store the nickname, title, story text and optional numbers you provide. We do not require your real name or email address. Please do not include personal contact details in your story.</p>
<h2>Cookies and advertising</h2>
<p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our site and other sites. You may opt out of personalized advertising by visiting <a href="https://adssettings.google.com">Google Ads Settings</a>. Where required by law, we request your consent before using non-essential cookies.</p>
<h2>Analytics and logs</h2>
<p>Our hosting provider may collect standard server logs such as IP address, browser type and pages visited for security and performance purposes.</p>
<h2>How we use information</h2>
<p>We use submitted stories to publish them (after review) on the community page, and we use technical data to keep the site working and secure. We do not sell personal information.</p>
<h2>Your choices</h2>
<p>To request removal of a story you submitted, email <a href="mailto:{EMAIL}">{EMAIL}</a> with the story title and nickname.</p>
<h2>Children</h2>
<p>This site is intended for adults and is not directed to children under 13.</p>
<h2>Changes</h2>
<p>We may update this policy and will change the date above when we do.</p>
</article></div></main>""")

page("terms.html", "Terms of Use | Lighter Together", "Terms of use for Lighter Together.",
f"""<main><div class="wrap"><article>
<h1>Terms of Use</h1>
<p class="meta">Last updated: {TODAY}</p>
<p>By using {SITE_NAME} you agree to these terms.</p>
<h2>Educational use only</h2>
<p>All content is for general information and is not medical advice. Do not delay or ignore professional medical advice because of something you read here.</p>
<h2>User stories</h2>
<p>By submitting a story you confirm it is your own experience, that it does not contain personal contact details, hateful, sexual or illegal content, or promotion of medicines, products or services. You grant us a non-exclusive license to display it on the site. We may edit, decline or remove any story at our discretion.</p>
<h2>No warranty</h2>
<p>The site is provided as is. We do not guarantee accuracy or results, and we are not liable for decisions made based on its content.</p>
<h2>Changes</h2>
<p>We may update these terms at any time.</p>
</article></div></main>""")

page("medical-disclaimer.html", "Medical Disclaimer | Lighter Together", "Medical disclaimer for Lighter Together.",
"""<main><div class="wrap"><article>
<h1>Medical Disclaimer</h1>
<p>The information on this website, including articles and user-submitted stories, is provided for educational purposes only. It is not a substitute for professional medical advice, diagnosis or treatment.</p>
<p>Always seek the advice of your physician or another qualified health provider with any questions about a medical condition, medication, diet or exercise program. Individual results vary, and the experiences shared by community members are personal and may not apply to you.</p>
<p>If you think you may have a medical emergency, call your local emergency services immediately.</p>
</article></div></main>""")

# ---------------- sitemap / robots ----------------
urls = "".join(f"<url><loc>{SITE_URL}/{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in pages)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT, "ads.txt"), "w").write("# Add after AdSense approval:\n# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
import shutil
shutil.copy("src/community.js", "dist/community.js")
page("ask.html", "Ask the Community | Lighter Together",
     "Ask questions about living with severe obesity and read answers from community members. All posts are reviewed before publishing.",
"""<main><div class="wrap"><h1>Ask the Community</h1>
<p>Ask a question or share what worked for you. This is peer support, not medical advice, so please talk to your doctor about medical decisions. All posts are reviewed before they appear.</p>
<div id="ask-board"></div></div></main>""")

print("built", len(pages), "pages")
