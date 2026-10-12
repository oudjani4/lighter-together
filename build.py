import os, shutil, datetime

SITE_NAME = "Lighter Together"
SITE_URL = "https://lighter-together.onrender.com"
EMAIL = "oudjanifarid4@gmail.com"
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
<p><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy-policy.html">Privacy Policy</a><a href="terms.html">Terms</a><a href="medical-disclaimer.html">Medical Disclaimer</a><a href="community-rules.html">Community Rules</a><a href="editorial-policy.html">Editorial Policy</a><a href="articles.html">Articles</a></p>
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
</article><h2>Community submissions</h2>
<p>When you submit a story, question, reply or report, we store what you type (your nickname, the text, and for stories the optional kilograms and months) in a Supabase database. Content you submit is reviewed and, once approved, becomes public on the site. Please do not include your real name, contact details or medical records. To have your content removed, email us at the address on the contact page.</p>
<p>We do not require accounts. Your browser stores a small timestamp locally to limit how often you can post. If advertising is shown on this site, advertising partners such as Google may use cookies to serve ads; you can manage this in your Google ad settings.</p>
</div></main>""")

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


page("community-rules.html", "Community Rules | Lighter Together",
     "The rules for posting stories, questions and replies on Lighter Together.",
"""<main><div class="wrap"><h1>Community Rules</h1>
<p>Lighter Together is a peer-support space. Please keep it kind, safe and honest.</p>
<ul>
<li><strong>Be respectful.</strong> No shaming, bullying, insults or comments about anyone's body.</li>
<li><strong>Protect your privacy.</strong> Use a nickname. Do not post your full name, phone number, address or medical records.</li>
<li><strong>No medical orders.</strong> Share your own experience, not instructions for others. Talk to your doctor before changing treatment, diet or medication.</li>
<li><strong>No selling or promotion.</strong> No ads, links to shops, supplements, or sources for prescription drugs.</li>
<li><strong>No dangerous advice.</strong> Posts that encourage extreme dieting, purging, or ignoring medical care will be removed.</li>
<li><strong>Be honest.</strong> Do not invent stories or results.</li>
</ul>
<h2>How moderation works</h2>
<p>Every story, question and reply is reviewed before it appears. Use the Report button on any answer or question that breaks these rules. We may edit or remove content at any time.</p>
<p>If you are in crisis or need urgent medical help, contact your local emergency number or a healthcare professional.</p>
<p>Questions or removal requests: <a href="contact.html">contact us</a>.</p>
</div></main>""")

page("editorial-policy.html", "Editorial Policy | Lighter Together",
     "How the guides on Lighter Together are written, sourced and corrected.",
"""<main><div class="wrap"><h1>Editorial Policy</h1>
<p>Lighter Together is run and edited by its owner. The site is an educational resource and a peer community. It is not a medical service.</p>
<h2>How we write</h2>
<ul>
<li>Guides are written in plain language and based on recognised public health sources, which are listed at the end of each article where possible.</li>
<li>We do not claim that articles are reviewed by doctors unless a named professional has actually done so.</li>
<li>We do not sell treatments or accept payment to recommend products.</li>
</ul>
<h2>Community content</h2>
<p>Stories, questions and replies are written by members and reflect personal experience only. They are not medical advice. See the <a href="community-rules.html">Community Rules</a>.</p>
<h2>Corrections</h2>
<p>If you find an error or outdated information, email <a href="mailto:%s">%s</a> and we will review and correct it.</p>
</div></main>""" % (EMAIL, EMAIL))


page("start-walking-with-severe-obesity.html",
     "How to Start Walking Safely With Severe Obesity | Lighter Together",
     "A gentle, practical plan for starting to walk when you live with severe obesity: how to begin, how to progress, and when to ask your doctor first.",
"""<main><div class="wrap"><article>
<h1>How to Start Walking Safely With Severe Obesity</h1>
<p class="meta">Educational content, not medical advice. Please read our <a href="medical-disclaimer.html">medical disclaimer</a>.</p>
<p>Walking is one of the simplest ways to become more active. It needs no equipment, can be done at any pace, and is usually gentler on the body than running. If severe obesity makes movement uncomfortable, the goal at the start is not speed or distance. It is to build a habit that feels safe and repeatable.</p>

<h2>Talk to your doctor first if...</h2>
<ul>
<li>you have heart or lung disease, diabetes, high blood pressure, or have not been active for a long time;</li>
<li>you have joint, back or foot pain, or problems with balance;</li>
<li>you take medicines that may affect your heart rate or blood sugar.</li>
</ul>
<p>Your doctor can tell you what is safe for you and whether to start with supervised sessions.</p>

<h2>Stop and get urgent help if you notice</h2>
<p>Chest pain or pressure, severe shortness of breath, fainting or severe dizziness, or sudden pain in a joint. Do not push through these.</p>

<h2>Week 1: start very small</h2>
<ul>
<li>Walk for 5 to 10 minutes at a comfortable pace, once or twice a day. Breaking activity into short sessions is fine.</li>
<li>Use the talk test: you should be able to talk, but not sing. If you cannot speak a full sentence, slow down.</li>
<li>Choose flat, even ground, or a treadmill, a mall, or a quiet street if the weather is difficult.</li>
<li>Rest whenever you need to. Stopping to rest is part of the plan, not a failure.</li>
</ul>

<h2>How to progress</h2>
<p>Once a session feels easy for a week or two, add a few minutes. Change only one thing at a time, either how long, how often, or how fast. The World Health Organization recommends that adults aim for 150 to 300 minutes of moderate-intensity activity a week, and stresses that some activity is better than none. Reaching that amount gradually, over weeks or months, is normal and sensible.</p>

<h2>Protect your joints and skin</h2>
<ul>
<li>Wear supportive, well-fitting shoes with cushioning and enough room for your toes.</li>
<li>Wear breathable clothing and moisture-wicking socks to reduce chafing. Anti-chafe products can help.</li>
<li>Drink water, and avoid walking in extreme heat.</li>
<li>If walking is painful, ask your doctor about lower-impact options such as water exercise, a stationary bike, or chair-based exercises.</li>
</ul>

<h2>Make it stick</h2>
<ul>
<li>Link walking to something you already do, such as after a meal or after a phone call.</li>
<li>Walk with a friend or family member, or share your progress with our <a href="ask.html">community</a>.</li>
<li>Track minutes, not weight. Better sleep, mood, energy and blood pressure can improve before the scale moves.</li>
</ul>

<h2>A realistic expectation</h2>
<p>Physical activity brings real health benefits even when weight changes slowly. On its own, it usually leads to modest weight loss, and it works best alongside medical care and healthy eating guided by a professional.</p>

<h2>Sources to read</h2>
<ul>
<li>World Health Organization: Guidelines on physical activity and sedentary behaviour (2020).</li>
<li>U.S. Centers for Disease Control and Prevention: Physical Activity Basics for Adults.</li>
<li>U.S. National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK): Physical activity and weight management.</li>
</ul>
<p class="meta">Written and edited by the owner of Lighter Together. See our <a href="editorial-policy.html">editorial policy</a>.</p>
</article></div></main>""")

page("articles.html", "Articles | Lighter Together",
     "Practical, plain-language articles about living with and treating severe obesity.",
"""<main><div class="wrap"><h1>Articles</h1>
<div class="card"><h3><a href="how-to-treat-severe-obesity.html">How to Treat Severe Obesity</a></h3><p>The main treatment options explained: evaluation, nutrition, activity, medication and surgery.</p></div>
<div class="card"><h3><a href="start-walking-with-severe-obesity.html">How to Start Walking Safely</a></h3><p>A gentle plan for beginning, progressing and staying safe.</p></div>\n<div class="card"><h3><a href="sleep-stress-and-weight.html">Sleep, Stress and Weight</a></h3><p>How rest and stress affect appetite, and simple steps to improve both.</p></div>
</div></main>""")


page("sleep-stress-and-weight.html",
     "Sleep, Stress and Weight: Why Rest Matters | Lighter Together",
     "How poor sleep and stress can affect appetite and weight, why the link works both ways, and simple steps to sleep and cope better.",
"""<main><div class="wrap"><article>
<h1>Sleep, Stress and Weight: Why Rest Matters</h1>
<p class="meta">Educational content, not medical advice. Please read our <a href="medical-disclaimer.html">medical disclaimer</a>.</p>
<p>Food and exercise get most of the attention, but sleep and stress also shape how hungry we feel and how much energy we have to move. Looking after them will not replace medical treatment, but it can make every other step easier.</p>

<h2>What the research suggests</h2>
<ul>
<li>Research links regularly sleeping less than about seven hours with a higher risk of gaining weight over time.</li>
<li>Short sleep appears to change hunger-related hormones and to raise the stress hormone cortisol later in the day, which can mean stronger cravings.</li>
<li>Reviews of the evidence also suggest that ongoing stress can increase appetite and cravings and lower motivation to be active.</li>
</ul>

<h2>It works both ways</h2>
<p>The link is not one-directional. Carrying extra weight can itself make sleep worse, through pain, discomfort, reflux, or breathing problems at night. So poor sleep is not a personal failing. It is part of a cycle that can be gently interrupted.</p>

<h2>See a doctor if you notice</h2>
<ul>
<li>loud snoring, choking or pauses in breathing during sleep, or waking with a headache;</li>
<li>heavy sleepiness during the day, even after a full night in bed;</li>
<li>low mood, constant worry or hopelessness that lasts for weeks.</li>
</ul>
<p>Sleep problems such as sleep apnea are common in people living with obesity and are treatable. Treating them can improve energy, mood and health.</p>

<h2>Small steps for better sleep</h2>
<ul>
<li>Go to bed and get up at about the same time every day, including weekends.</li>
<li>Keep the bedroom dark, quiet and cool, and put screens away for the last hour before bed.</li>
<li>Avoid caffeine in the afternoon and large meals close to bedtime.</li>
<li>A short daily walk, especially in daylight, can help you fall asleep more easily.</li>
</ul>

<h2>Small steps for stress</h2>
<ul>
<li>Try slow breathing for two to five minutes: breathe in gently, then breathe out for longer than you breathe in.</li>
<li>Notice when you eat because of stress rather than hunger, and keep a short list of other things to try first, such as a walk, a call to a friend, or a glass of water.</li>
<li>Talk to someone you trust, to a counsellor, or to our <a href="ask.html">community</a>. You do not have to carry it alone.</li>
</ul>

<h2>Sources to read</h2>
<ul>
<li>Geiker NRW et al. Does stress influence sleep patterns, food intake, weight gain, abdominal obesity and weight loss interventions and vice versa? Obesity Reviews, 2018.</li>
<li>U.S. National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK): Sleep Extension Study in obese adults with short sleep duration (ClinicalTrials.gov NCT00261898).</li>
</ul>
<p class="meta">Written and edited by the owner of Lighter Together. See our <a href="editorial-policy.html">editorial policy</a>.</p>
</article></div></main>""")

print("built", len(pages), "pages")
