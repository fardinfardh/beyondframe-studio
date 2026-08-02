#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site builder for Beyond Frame.
Wraps page-specific CONTENT strings with a shared HEAD / HEADER / FOOTER / SCRIPTS chrome
and writes plain .html files. No runtime templating in the browser — output is
plain static HTML, good for SEO and reliability on Cloudflare Pages.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("the-method.html", "The Method"),
    ("programs.html", "Programs"),
    ("direction-session.html", "Direction Session"),
    ("about.html", "About"),
    ("testimonials.html", "Testimonials"),
    ("contact.html", "Contact"),
]

WA_NUMBER = "31655935251"

WA_BUTTON = f'''
  <a class="wa-float" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 32 32" fill="#fff" xmlns="http://www.w3.org/2000/svg"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.386.697 4.607 1.898 6.48L4 29l7.72-1.865A11.93 11.93 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3zm6.994 16.99c-.294.828-1.457 1.517-2.386 1.716-.635.135-1.464.243-4.257-.914-3.573-1.48-5.873-5.104-6.053-5.342-.173-.239-1.457-1.939-1.457-3.698 0-1.759.92-2.623 1.246-2.984.326-.36.71-.45.947-.45.237 0 .474.002.68.012.218.01.512-.083.8.61.294.708 1 2.443 1.087 2.622.087.18.146.39.03.63-.116.24-.174.39-.347.6-.174.21-.365.469-.522.63-.174.18-.355.375-.153.735.202.36.897 1.48 1.925 2.397 1.324 1.18 2.44 1.545 2.8 1.72.36.174.57.15.78-.09.21-.24.897-1.046 1.137-1.404.24-.36.48-.3.81-.18.33.12 2.093.987 2.452 1.166.36.18.6.27.687.42.087.15.087.87-.208 1.698z"/></svg>
  </a>
'''

def head(title, desc, path):
    depth = ""  # all files at root, so relative paths are flat
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://beyondframe.studio/{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="/assets/images/BeyondFrame.jpg">
<meta property="og:url" content="https://beyondframe.studio/{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/images/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
'''

def header(active):
    def nav_link(href, label):
        cls = ' class="active"' if href == active else ''
        return f'      <a href="/{href}"{cls}>{label}</a>'
    links = "\n".join(nav_link(href, label) for href, label in NAV)
    mobile_links = "\n".join(
        f'      <a href="/{href}">{label}</a>'
        for href, label in NAV
    )
    return f'''
<header class="site-header" id="site-header">
  <div class="container header-inner">
    <a href="/" class="brand">Beyond Frame <small>Photography Mentorship</small></a>
    <nav class="main-nav">
{links}
    </nav>
    <div class="header-cta">
      <a href="/booking.html" class="btn btn-primary">Book a Session</a>
      <button class="nav-toggle" aria-label="Menu"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-nav">
{mobile_links}
  <a href="/booking.html" class="btn btn-primary mobile-cta">Book a Direction Session</a>
  <div class="mobile-meta">hello@beyondframe.studio &nbsp;·&nbsp; Worldwide, Online</div>
</div>
'''

FOOTER = '''
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="brand">Beyond Frame</div>
        <p>A private one-to-one photography mentorship, guided by Hossein Fardinfard. Identity, image-making, presentation, and opportunity &mdash; worldwide, online.</p>
      </div>
      <div class="footer-col">
        <h5>Explore</h5>
        <ul>
          <li><a href="/the-method.html">The Method</a></li>
          <li><a href="/programs.html">Programs</a></li>
          <li><a href="/direction-session.html">Direction Session</a></li>
          <li><a href="/booking.html">Book a Session</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Studio</h5>
        <ul>
          <li><a href="/about.html">About</a></li>
          <li><a href="/testimonials.html">Testimonials</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="https://hossein.art" target="_blank" rel="noopener">Photography Work &#8599;</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Legal</h5>
        <ul>
          <li><a href="/terms.html">Terms &amp; Conditions</a></li>
          <li><a href="/privacy.html">Privacy Policy</a></li>
          <li><a href="/refund.html">Refund Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; <span id="year">2026</span> Beyond Frame &mdash; Orange Luna L.L.C-FZ, Dubai, UAE</div>
      <div class="footer-social">
        <a href="mailto:hello@beyondframe.studio">hello@beyondframe.studio</a>
        <a href="https://www.instagram.com/hossein.foto" target="_blank" rel="noopener">Instagram</a>
        <a href="https://wa.me/31655935251" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </div>
</footer>
'''

SCRIPTS = '''
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="/assets/js/main.js"></script>
'''

def write_page(path, title, desc, active, content):
    html = head(title, desc, path) + "<body>\n" + header(active) + "\n<main>\n" + content + "\n</main>\n" + FOOTER + WA_BUTTON + SCRIPTS + "\n</body>\n</html>\n"
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)

PAGES = []

def page(path, title, desc, active, content):
    PAGES.append((path, title, desc, active, content))

# ---- HOME ----
page("index.html",
  "Beyond Frame — Photography Mentorship by Hossein Fardinfard",
  "Private one-on-one photography mentorship with Hossein Fardinfard. Develop your creative direction, image-making, and portfolio for photographers worldwide.",
  "index.html",
  '''
<section class="hero">
  <div class="hero-media"><img src="/assets/images/home/Beyond_Frame_Hero.webp" alt="Portrait photography by Hossein Fardinfard" loading="eager"></div>
  <div class="container hero-content">
    <p class="eyebrow reveal">Private Photography Mentorship &mdash; Worldwide, Online</p>
    <h1 class="hero-title reveal reveal-delay-1">Photography didn&rsquo;t just teach me to make images. It taught me to understand myself.</h1>
    <p class="hero-sub reveal reveal-delay-2">A private mentorship for photographers who want clarity, direction, and a stronger relationship with their own work &mdash; guided one to one by Hossein Fardinfard.</p>
    <div class="hero-actions reveal reveal-delay-3">
      <a href="/direction-session.html" class="btn btn-primary">Start With a Direction Session <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      <a href="/the-method.html" class="btn btn-outline-light">Learn the Method</a>
    </div>
    <div class="hero-scroll"><span class="line"></span> Scroll</div>
  </div>
</section>

<section class="section-sm bg-paper">
  <div class="container statement reveal text-center center-col">
    <p>One path for everyone: <em>a Direction Session</em>, a written proposal, and a program built <em>only for you.</em></p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split-media media-frame reveal">
      <img src="/assets/images/home/A_Personal_Note.webp" alt="Hossein Fardinfard, founder of Beyond Frame">
    </div>
    <div class="reveal reveal-delay-1">
      <p class="eyebrow">A Personal Note</p>
      <h2>Photography has never been only about images for me.</h2>
      <p style="margin-top:22px;color:var(--ink-soft);font-size:1.05rem;line-height:1.75;">It has always been connected to people, questions, uncertainty, and the way we try to understand ourselves through what we create. Through years of teaching and reviewing photographic work, I noticed that most photographers aren&rsquo;t held back by technique &mdash; more often, they struggle with direction, confidence, and understanding what genuinely belongs to them.</p>
      <p style="margin-top:16px;color:var(--ink-soft);font-size:1.05rem;line-height:1.75;">Beyond Frame grew out of one question that kept returning in every conversation: <em class="serif" style="color:var(--clay);">&ldquo;Why are you making these photographs?&rdquo;</em></p>
      <a href="/about.html" class="btn btn-ghost" style="margin-top:28px;">Read My Full Story</a>
    </div>
  </div>
</section>

<section class="section bg-cream-soft">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Is This For You?</p>
      <h2>You might recognise yourself here.</h2>
      <ul class="pillar-list" style="margin-top:28px;font-size:1.02rem;">
        <li>You feel stuck, or unsure what to focus on next</li>
        <li>You&rsquo;ve learned the technical side, but your work still feels generic</li>
        <li>You struggle to explain what your photography is actually about</li>
        <li>You want a portfolio and a way of presenting yourself that feels honest</li>
        <li>You&rsquo;re ready for real feedback, not just encouragement</li>
      </ul>
      <a href="/direction-session.html" class="btn btn-primary" style="margin-top:32px;">Get Clarity in a Direction Session</a>
    </div>
    <div class="split-media media-frame reveal reveal-delay-1">
      <img src="/assets/images/home/Is This For You.webp" alt="Photographer reviewing work with Hossein Fardinfard">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center reveal">
      <p class="eyebrow">The Method</p>
      <h2>Four pillars. One path shaped around you.</h2>
      <p>Every Beyond Frame program moves through the same framework, in depth or in overview &mdash; identity, image-making, presentation, and opportunity.</p>
    </div>
    <div class="grid grid-4 reveal reveal-delay-1">
      <div><span class="pillar-num" style="font-size:1.8rem;">01</span><h3 style="font-size:1.2rem;margin:8px 0 10px;">Identity &amp; Direction</h3><p style="color:var(--ink-soft);font-size:.92rem;line-height:1.6;">Find what truly belongs to you.</p></div>
      <div><span class="pillar-num" style="font-size:1.8rem;">02</span><h3 style="font-size:1.2rem;margin:8px 0 10px;">Image-Making</h3><p style="color:var(--ink-soft);font-size:.92rem;line-height:1.6;">Turn ideas into images with intention.</p></div>
      <div><span class="pillar-num" style="font-size:1.8rem;">03</span><h3 style="font-size:1.2rem;margin:8px 0 10px;">Presentation</h3><p style="color:var(--ink-soft);font-size:.92rem;line-height:1.6;">Present your work with confidence.</p></div>
      <div><span class="pillar-num" style="font-size:1.8rem;">04</span><h3 style="font-size:1.2rem;margin:8px 0 10px;">Opportunities</h3><p style="color:var(--ink-soft);font-size:.92rem;line-height:1.6;">Build a sustainable, real-world practice.</p></div>
    </div>
    <div class="text-center reveal reveal-delay-2" style="margin-top:48px;"><a href="/the-method.html" class="btn btn-outline">See the Four Pillars in Detail</a></div>
  </div>
</section>

<section class="quote-block bg-ink">
  <div class="hero-media" style="opacity:.22;"><img src="/assets/images/home/BeyondFrame_Quote_1.webp" alt=""></div>
  <div class="container reveal" style="position:relative;">
    <blockquote>&ldquo;I believe good photography begins with understanding yourself. When you know what matters to you, your images become honest, consistent, and powerful.&rdquo;<cite>Hossein Fardinfard &mdash; Founder, Beyond Frame</cite></blockquote>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header reveal">
      <p class="eyebrow">A Glimpse of the Work</p>
      <h2>Photography by Hossein Fardinfard.</h2>
    </div>
    <div class="grid grid-4 reveal reveal-delay-1">
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/home/P022.webp" alt="Portrait photography"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/home/P06.webp" alt="Documentary photography"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/home/P077.webp" alt="Portrait photography"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/home/P088.webp" alt="Documentary photography"></div>
    </div>
    <div class="text-center reveal reveal-delay-2" style="margin-top:40px;"><a href="https://hossein.art" target="_blank" rel="noopener" class="btn btn-ghost">View the Full Portfolio &nbsp;&#8599;</a></div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-header center reveal">
      <p class="eyebrow">In Their Words</p>
      <h2>Reflections from the journey.</h2>
    </div>
    <div class="grid grid-2 reveal reveal-delay-1">
      <div class="testi-card">
        <div class="testi-avatar"><img src="/assets/images/testimonials/Teona.jpg" alt="Teona Machavariani"></div>
        <p class="testi-text">&ldquo;What begins as a conversation about images often turns into a conversation about the person making them &mdash; an experience that continues to shape the way I work.&rdquo;</p>
        <div class="testi-name" style="margin-top:18px;font-size:1rem;">Teona Machavariani</div>
      </div>
      <div class="testi-card">
        <div class="testi-avatar"><img src="/assets/images/testimonials/Talal.jpg" alt="Talal Mansoor"></div>
        <p class="testi-text">&ldquo;He teaches in a way no other photography course does: he first helps you find your inner artist.&rdquo;</p>
        <div class="testi-name" style="margin-top:18px;font-size:1rem;">Talal Mansoor</div>
      </div>
    </div>
    <div class="text-center reveal reveal-delay-2" style="margin-top:40px;"><a href="/testimonials.html" class="btn btn-ghost">Read All Testimonials</a></div>
  </div>
</section>

<section class="quote-block bg-ink">
  <div class="hero-media" style="opacity:.22;"><img src="/assets/images/home/BeyondFrame_Quote_2.webp" alt=""></div>
  <div class="container reveal" style="position:relative;">
    <blockquote>&ldquo;My role is not to tell you who to become. It is to help you uncover what is already there.&rdquo;<cite>The Beyond Frame Approach</cite></blockquote>
  </div>
</section>

<section class="cta-band">
  <div class="container reveal">
    <p class="eyebrow">Ready When You Are</p>
    <h2>Ready to see what your program would look like?</h2>
    <div class="cta-actions">
      <a href="/booking.html" class="btn btn-primary">Book Your Direction Session</a>
      <a href="/programs.html" class="btn btn-outline">Explore Programs</a>
    </div>
  </div>
</section>
'''
)

# ---- THE METHOD ----
page("the-method.html",
  "The Four Pillars — The Beyond Frame Method",
  "A structured mentorship method built on four pillars: identity and direction, image-making, presentation, and opportunities. Learn how it works.",
  "the-method.html",
  '''
<section class="page-hero dark">
  <div class="container reveal">
    <p class="eyebrow">The Method</p>
    <h1 class="page-hero-title">The Four Pillars</h1>
    <p class="lead">Photography is more than making images. It is understanding yourself, developing your ideas, communicating your work, and finding your place in the photographic world. These pillars aren&rsquo;t about making you look like other photographers &mdash; they&rsquo;re about helping you become more yourself.</p>
  </div>
</section>

<section class="section">
  <div class="container">

    <div class="pillar reveal">
      <div class="pillar-num">01</div>
      <div class="pillar-body">
        <h3 class="pillar-head">Identity &amp; Direction</h3>
        <p class="pillar-tagline">Find what truly belongs to you &mdash; the foundation everything else builds on.</p>
        <p>Without identity, photography becomes random effort. When it&rsquo;s clear, motivation, confidence, and authenticity grow on their own.</p>
        <p class="eyebrow" style="margin-top:20px;">We Work On</p>
        <ul class="pillar-list">
          <li>Recurring themes &amp; obsessions</li>
          <li>Influence vs. imitation</li>
          <li>Documentary, art, commercial, editorial paths</li>
          <li>Building motivation &amp; discipline</li>
        </ul>
        <p class="eyebrow">You&rsquo;ll Leave With</p>
        <ul class="pillar-list">
          <li>A written direction statement</li>
          <li>A real project idea, not a vague one</li>
          <li>Readiness to start producing work</li>
        </ul>
        <div class="pillar-transition"><strong>Transition &rarr;</strong> Guided First Photo Series &mdash; a small personal project that turns identity work into real practice.</div>
      </div>
      <div class="pillar-side">
        <p class="pillar-meta">6 Sessions &middot; 75 Min Each</p>
        <div class="pillar-price">$520</div>
        <p class="pillar-meta">As a Single Pillar</p>
      </div>
    </div>

    <div class="pillar reveal">
      <div class="pillar-num">02</div>
      <div class="pillar-body">
        <h3 class="pillar-head">Image-Making</h3>
        <p class="pillar-tagline">Turn ideas into images that carry your intention.</p>
        <p>Strong ideas without visual language stay invisible. This pillar makes inner depth visible through real shooting, not lectures.</p>
        <p class="eyebrow" style="margin-top:20px;">We Work On</p>
        <ul class="pillar-list">
          <li>Learning technical skills by doing, not theory</li>
          <li>Reading &amp; critiquing images</li>
          <li>Editing choices that support identity</li>
        </ul>
        <p class="eyebrow">You&rsquo;ll Leave With</p>
        <ul class="pillar-list">
          <li>A more consistent, recognisable style</li>
          <li>A refined body of work</li>
          <li>Confidence reading your own images</li>
        </ul>
        <div class="pillar-transition"><strong>Transition &rarr;</strong> Portfolio Formation &mdash; your strongest work refined into a body of work ready to present.</div>
      </div>
      <div class="pillar-side">
        <p class="pillar-meta">8 Sessions &middot; 75 Min Each</p>
        <div class="pillar-price">$760</div>
        <p class="pillar-meta">As a Single Pillar</p>
      </div>
    </div>

    <div class="pillar reveal">
      <div class="pillar-num">03</div>
      <div class="pillar-body">
        <h3 class="pillar-head">Presentation</h3>
        <p class="pillar-tagline">How your work is presented shapes how it is understood.</p>
        <p>Many talented photographers stay unseen &mdash; not for lack of skill, but because they don&rsquo;t know how to present themselves.</p>
        <p class="eyebrow" style="margin-top:20px;">We Work On</p>
        <ul class="pillar-list">
          <li>Portfolio selection &amp; sequencing</li>
          <li>Bio vs. artist statement</li>
          <li>Website essentials, pitching, pricing</li>
        </ul>
        <p class="eyebrow">You&rsquo;ll Leave With</p>
        <ul class="pillar-list">
          <li>A focused, professional portfolio</li>
          <li>Clear language to talk about your work</li>
          <li>Real outreach experience</li>
        </ul>
        <div class="pillar-transition"><strong>Transition &rarr;</strong> Real Outreach Practice &mdash; contacting real galleries, brands, and publications with your portfolio.</div>
      </div>
      <div class="pillar-side">
        <p class="pillar-meta">6 Sessions &middot; 75 Min Each</p>
        <div class="pillar-price">$820</div>
        <p class="pillar-meta">As a Single Pillar</p>
      </div>
    </div>

    <div class="pillar reveal">
      <div class="pillar-num">04</div>
      <div class="pillar-body">
        <h3 class="pillar-head">Opportunities</h3>
        <p class="pillar-tagline">Talent alone rarely creates sustainability.</p>
        <p>Many strong photographers struggle not from lack of talent, but from misunderstanding the system around them.</p>
        <p class="eyebrow" style="margin-top:20px;">We Work On</p>
        <ul class="pillar-list">
          <li>Clients, galleries, magazines, grants</li>
          <li>Teaching, licensing &amp; stock as income</li>
          <li>Networking &amp; long-term reputation</li>
        </ul>
        <p class="eyebrow">You&rsquo;ll Leave With</p>
        <ul class="pillar-list">
          <li>A realistic income model</li>
          <li>A 12-month opportunity roadmap</li>
          <li>Confidence approaching people</li>
        </ul>
      </div>
      <div class="pillar-side">
        <p class="pillar-meta">8 Sessions &middot; 75 Min Each</p>
        <div class="pillar-price">$1,020</div>
        <p class="pillar-meta">As a Single Pillar</p>
      </div>
    </div>

  </div>
</section>

<section class="cta-band bg-cream-soft">
  <div class="container reveal">
    <p class="eyebrow">See How These Combine</p>
    <h2>Compact overview, one focused pillar, or the complete journey &mdash; all built on this same method.</h2>
    <div class="cta-actions"><a href="/programs.html" class="btn btn-primary">See Programs &amp; Pricing</a></div>
  </div>
</section>
'''
)

# ---- PROGRAMS ----
page("programs.html",
  "Photography Mentorship Programs & Pricing — Beyond Frame",
  "Choose from single sessions to a complete 24-session mentorship. Compare programs, pillars, and pricing for one-on-one online photography guidance.",
  "programs.html",
  '''
<section class="page-hero dark">
  <div class="container reveal">
    <p class="eyebrow">Programs &amp; How It Works</p>
    <h1 class="page-hero-title">Your Program Doesn&rsquo;t Exist Yet. That&rsquo;s the Point.</h1>
    <p class="lead">Most mentorships ask you to choose a package before anyone has seen your work. Beyond Frame works the other way around: first we understand where you are, then you receive a written proposal for a program designed only for you &mdash; its focus, its length, and its exact price.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header reveal">
      <p class="eyebrow">How It Works</p>
      <h2>Three steps, always in this order.</h2>
      <p>Every mentorship begins with a Direction Session (USD 90). If you continue into a program, the 90 is deducted from your program price.</p>
    </div>
    <div class="steps reveal reveal-delay-1">
      <div class="step">
        <div class="step-num">Step 01</div>
        <div>
          <h3>The Direction Session</h3>
          <p>A private 60-minute call on Google Meet. Before we meet, you send 10&ndash;15 images and a few notes about your goals and frustrations. In the session we look honestly at where you are, what is holding you back, and what genuinely deserves your focus next.</p>
          <p class="meta-line">60 Minutes &middot; Online &middot; USD 90 (credited toward your program)</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">Step 02</div>
        <div>
          <h3>Your Written Proposal</h3>
          <p>Within 48 hours of your session, you receive a one-page written proposal containing an honest summary of where you are now, the 2&ndash;3 areas your program will focus on, the number of sessions and cadence, the final deliverable, and the exact price &mdash; with the USD 90 already deducted.</p>
          <p class="meta-line">Valid for 14 Days &middot; No Obligation</p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">Step 03</div>
        <div>
          <h3>Your Personal Program</h3>
          <p>Programs are built from the Four Pillars framework and shaped entirely around your needs &mdash; private 75-minute sessions on Google Meet, a written summary and assignment after every session, ongoing feedback between sessions, and a concrete final deliverable.</p>
          <p class="meta-line">4&ndash;24 Sessions &middot; Most Between USD 780&ndash;2,900 &middot; Stripe Payment, Full or Installments</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-header center reveal">
      <p class="eyebrow">Choose Your Depth</p>
      <h2>Every photographer is at a different stage.</h2>
      <p>Some need clarity before going deeper. Some want to focus on one specific challenge. Others are ready for full, long-term development. All three options work through the same four-pillar method &mdash; the difference is simply how deep you go.</p>
    </div>

    <div class="program-cards reveal reveal-delay-1">
      <div class="program-card">
        <p class="eyebrow">For a Quick Overview</p>
        <h3>Compact Program</h3>
        <p class="desc">A short overview of all four pillars, so you get clarity before going deeper.</p>
        <div class="price">$440</div>
        <div class="duration">4 Sessions &middot; 75 Min Each &middot; 4&ndash;6 Weeks</div>
        <ul>
          <li><span class="tick">&#10003;</span><span><strong>Explore your direction</strong>Look at what your work is about and where it could go.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>See what your images need</strong>A quick review of your photos and what to improve.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Understand strong presentation</strong>See what makes a portfolio work, without building one yet.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Get your personal roadmap</strong>Leave knowing your strengths, gaps, and best next step.</span></li>
        </ul>
        <a href="/contact.html" class="btn btn-outline">Apply</a>
      </div>

      <div class="program-card featured">
        <p class="eyebrow">For Long-Term Growth</p>
        <h3>Complete Program</h3>
        <p class="desc">All four pillars in one connected journey, from first ideas to a finished body of work.</p>
        <div class="price">$2,790</div>
        <div class="duration">24 Sessions &middot; 75 Min Each &middot; ~6 Months</div>
        <ul>
          <li><span class="tick">&#10003;</span><span><strong>Find your direction</strong>Discover what photography is really about.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Make stronger images</strong>Turn your ideas into personal, consistent work.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Build your portfolio</strong>Learn how to present it professionally.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Build a career</strong>Learn how the industry works and how to earn from your work.</span></li>
        </ul>
        <a href="/contact.html" class="btn btn-primary">Apply</a>
      </div>

      <div class="program-card">
        <p class="eyebrow">For One Specific Goal</p>
        <h3>Single Pillar</h3>
        <p class="desc">Already know what you want to improve? Go deep on just one pillar.</p>
        <div class="price">from $520</div>
        <div class="duration">6&ndash;8 Sessions &middot; 75 Min Each</div>
        <ul>
          <li><span class="tick">&#10003;</span><span><strong>Choose one focus area</strong>Pick the pillar that matters most to you.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Go deep on that goal</strong>Assignments built around your chosen area.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>Get continuous feedback</strong>Support between every session.</span></li>
          <li><span class="tick">&#10003;</span><span><strong>See pricing below</strong>Full descriptions and prices per pillar.</span></li>
        </ul>
        <a href="#single-pillar" class="btn btn-outline">See Pillars</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="single-pillar">
  <div class="container">
    <div class="section-header reveal">
      <p class="eyebrow">Single Pillar &mdash; Choose Your Focus</p>
      <h2>Each pillar is a complete focus area on its own.</h2>
      <p>Pricing differs because some pillars need more preparation and feedback between sessions.</p>
    </div>
    <div class="pillar-pick reveal reveal-delay-1">
      <div>
        <span class="tag">Pillar 01</span>
        <h4>Identity &amp; Direction</h4>
        <p>Discover your recurring themes, understand what your work is about, and leave with a clear project direction.</p>
        <div class="price">$520</div>
        <div class="sessions">6 Sessions</div>
      </div>
      <div>
        <span class="tag">Pillar 02</span>
        <h4>Image-Making</h4>
        <p>Improve light, composition, and storytelling inside your own photos, and build a style people recognise.</p>
        <div class="price">$760</div>
        <div class="sessions">8 Sessions</div>
      </div>
      <div>
        <span class="tag">Pillar 03</span>
        <h4>Presentation</h4>
        <p>Select and order your best work, write your bio and artist statement, and present yourself professionally.</p>
        <div class="price">$820</div>
        <div class="sessions">6 Sessions</div>
      </div>
      <div>
        <span class="tag">Pillar 04</span>
        <h4>Opportunities</h4>
        <p>Learn how the industry works, from clients and galleries to grants and income, and build a realistic plan.</p>
        <div class="price">$1,020</div>
        <div class="sessions">8 Sessions</div>
      </div>
    </div>
    <p class="text-center reveal reveal-delay-2" style="margin-top:36px;color:var(--ink-soft);">Want the full picture? <a href="/the-method.html" class="btn-ghost" style="display:inline;border-bottom:1px solid var(--ink);">Read the Four Pillars in detail &rarr;</a></p>
  </div>
</section>

<section class="section bg-cream-soft">
  <div class="container">
    <div class="section-header center reveal">
      <p class="eyebrow">Before You Apply</p>
      <h2>A few common questions.</h2>
    </div>
    <div class="faq-list reveal reveal-delay-1" style="max-width:820px;margin:0 auto;">
      <div class="faq-item">
        <button class="faq-q"><span>How do sessions work?</span><span class="plus"></span></button>
        <div class="faq-a"><div class="faq-a-inner">Private, one to one, 75 minutes, live on Google Meet. Between sessions you get assignments, written feedback, and can reach me on WhatsApp or email.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>Why is there no price list?</span><span class="plus"></span></button>
        <div class="faq-a"><div class="faq-a-inner">Because no two photographers need the same program. Your proposal states the exact price before you commit to anything.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>What if I only want the Direction Session?</span><span class="plus"></span></button>
        <div class="faq-a"><div class="faq-a-inner">That is completely fine. It stands on its own &mdash; you leave with real clarity about your work and next step, with zero pressure to continue.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q"><span>What is the refund policy?</span><span class="plus"></span></button>
        <div class="faq-a"><div class="faq-a-inner">Full details are on our <a href="/refund.html" style="text-decoration:underline;">Refund Policy page</a>, summarised before you book, so there are no surprises.</div></div>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container reveal">
    <p class="eyebrow">Ready to Apply, or Want a Recommendation First?</p>
    <h2>Ready to see what your program would look like?</h2>
    <div class="cta-actions">
      <a href="/booking.html" class="btn btn-primary">Book Direction Session</a>
      <a href="/contact.html" class="btn btn-outline">Apply for a Program</a>
    </div>
  </div>
</section>
'''
)

# ---- DIRECTION SESSION ----
page("direction-session.html",
  "Direction Session — Beyond Frame",
  "A private one-to-one photography direction session designed to help photographers gain clarity, identify challenges, and define their next steps.",
  "direction-session.html",
  '''
<section class="page-hero dark" style="padding-top:190px;">
  <div class="hero-media" style="opacity:.32;"><img src="/assets/images/direction_session/DIrection_session_hero.webp" alt=""></div>
  <div class="container reveal" style="position:relative;">
    <p class="eyebrow">Not Sure What Your Next Step Is?</p>
    <h1 class="page-hero-title">Get Clarity on Your Work, Your Direction, and Your Next Step.</h1>
    <p class="lead">A private one-to-one session for photographers who feel stuck, unsure what to focus on next, or uncertain which path makes the most sense for them.</p>
    <div class="hero-actions" style="margin-top:34px;"><a href="/booking.html" class="btn btn-primary">Book Your Direction Session</a></div>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="grid grid-3 reveal">
      <div class="testi-card" style="text-align:center;"><p class="eyebrow">Format</p><h3 style="margin-top:10px;">60 Minutes</h3><p style="color:var(--ink-soft);margin-top:6px;">One-to-One</p></div>
      <div class="testi-card" style="text-align:center;"><p class="eyebrow">Where</p><h3 style="margin-top:10px;">Online</h3><p style="color:var(--ink-soft);margin-top:6px;">Live Session, Google Meet</p></div>
      <div class="testi-card" style="text-align:center;"><p class="eyebrow">Investment</p><h3 style="margin-top:10px;">USD 90</h3><p style="color:var(--ink-soft);margin-top:6px;">Credited Toward Your Program</p></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Sometimes You Simply Need Clarity</p>
      <h2>Sometimes the next step isn&rsquo;t another course, portfolio review, or workshop.</h2>
      <p style="margin-top:22px;color:var(--ink-soft);font-size:1.05rem;line-height:1.75;">This session is for photographers who feel stuck, unsure what to focus on next, or uncertain about which path makes the most sense for them. Together, we look at where you are now, what is holding you back, and what your next step could be.</p>
      <p class="eyebrow" style="margin-top:32px;">During the Session, We Talk Through</p>
      <ul class="pillar-list" style="margin-top:16px;">
        <li>Where you are in your photography today</li>
        <li>What feels unclear, difficult, or frustrating</li>
        <li>What you want to build, explore, or improve</li>
      </ul>
    </div>
    <div class="split-media media-frame reveal reveal-delay-1">
      <img src="/assets/images/direction_session/Direction_Session_Band.webp" alt="Direction Session with Hossein Fardinfard">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center reveal">
      <p class="eyebrow">What You&rsquo;ll Leave With</p>
      <h2>Greater clarity about your work, and your next step.</h2>
    </div>
    <div class="grid grid-3 reveal reveal-delay-1">
      <div><h3 style="font-size:1.15rem;">Your Direction</h3><p style="color:var(--ink-soft);margin-top:10px;font-size:.95rem;">A clearer understanding of what your work is really about.</p></div>
      <div><h3 style="font-size:1.15rem;">Your Main Gaps</h3><p style="color:var(--ink-soft);margin-top:10px;font-size:.95rem;">Honest clarity on what is genuinely holding you back.</p></div>
      <div><h3 style="font-size:1.15rem;">What to Focus On Next</h3><p style="color:var(--ink-soft);margin-top:10px;font-size:.95rem;">Whether a focused program, complete program, or independent work is right for you.</p></div>
    </div>
    <div class="statement reveal reveal-delay-2 text-center center-col" style="margin-top:64px;">
      <p style="font-size:1.4rem;">This session stands on its own. Whether you continue with a program or not, you will leave with greater clarity about your work and your next step.</p>
    </div>
  </div>
</section>

<section class="cta-band bg-cream-soft">
  <div class="container reveal">
    <div class="cta-actions"><a href="/booking.html" class="btn btn-primary">Book Your Direction Session &mdash; USD 90</a></div>
  </div>
</section>
'''
)

# ---- BOOKING ----
page("booking.html",
  "Book a Direction Session — Beyond Frame",
  "Book your private Direction Session with Hossein Fardinfard. Choose your time and pay securely — powered by Calendly and Stripe.",
  "booking.html",
  '''
<section class="page-hero dark" style="padding-top:190px;padding-bottom:70px;">
  <div class="container reveal">
    <p class="eyebrow">Book Your Session</p>
    <h1 class="page-hero-title">Book a Direction Session</h1>
    <p class="lead">Choose a time that works for you below. You&rsquo;ll answer a few short questions and pay securely by card &mdash; your session is confirmed the moment payment goes through.</p>
  </div>
</section>

<section class="section-sm">
  <div class="container booking-wrap">
    <aside class="booking-summary reveal">
      <p class="eyebrow">Session Summary</p>
      <h3 style="margin-top:10px;">Direction Session</h3>
      <p style="color:var(--ink-soft);margin-top:10px;font-size:.95rem;line-height:1.6;">A focused one-to-one session for photographers who feel uncertain about their direction, stuck in their process, or unsure what to focus on next.</p>
      <div class="price">USD 90</div>
      <ul>
        <li><span class="tick">&#10003;</span> 60-minute live session, Google Meet</li>
        <li><span class="tick">&#10003;</span> Personalised guidance &amp; feedback</li>
        <li><span class="tick">&#10003;</span> Clarity on your next steps</li>
        <li><span class="tick">&#10003;</span> Credited toward a program, if you continue</li>
      </ul>
      <p class="form-note">Payment is collected securely through Stripe as part of the Calendly booking flow. By booking, you agree to our <a href="/terms.html" style="text-decoration:underline;">Terms</a>, <a href="/refund.html" style="text-decoration:underline;">Refund Policy</a>, and <a href="/privacy.html" style="text-decoration:underline;">Privacy Policy</a>.</p>
    </aside>
    <div class="reveal reveal-delay-1">
      <div class="calendly-shell" id="calendly-embed" data-url="https://calendly.com/hello-beyondframe/direction-session?hide_gdpr_banner=1&background_color=faf7f1&text_color=171512&primary_color=a8481f">
        <div class="cal-loading"><div class="spinner"></div>Loading availability&hellip;</div>
      </div>
    </div>
  </div>
</section>
'''
)

# ---- ABOUT ----
page("about.html",
  "About Hossein Fardinfard — Beyond Frame",
  "Learn more about Hossein Fardinfard, documentary photographer and educator behind Beyond Frame, and his approach to photography education and development.",
  "about.html",
  '''
<section class="page-hero dark">
  <div class="container reveal">
    <p class="eyebrow">About Me</p>
    <h1 class="page-hero-title">Hossein Fardinfard</h1>
    <p class="lead">Portrait &amp; documentary photographer. Educator. Mentor.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split-media media-frame reveal">
      <img src="/assets/images/about/About_HosseinFardinfard.webp" alt="Hossein Fardinfard, portrait photographer and mentor">
    </div>
    <div class="reveal reveal-delay-1">
      <p>Photography has never been only about images for me. It has always been connected to people, questions, uncertainty, identity, and the way we try to understand ourselves through what we create.</p>
      <p style="margin-top:18px;">Over the years, my work as a documentary photographer led me to different countries, stories, and experiences &mdash; and eventually to studying photography at the Royal Academy of Art in The Hague, Netherlands. Alongside photography itself, I found myself increasingly interested in teaching, conversations, and helping others move through creative uncertainty.</p>
      <p style="margin-top:18px;">Through years of teaching, mentoring, and reviewing photographic work, I noticed that many photographers are not held back by technique. More often, they struggle with direction, confidence, and understanding what genuinely belongs to them.</p>
    </div>
  </div>
</section>

<section class="quote-block bg-ink">
  <div class="container reveal">
    <blockquote>&ldquo;Why are you making these photographs?&rdquo;</blockquote>
    <p style="max-width:70ch;margin-top:24px;color:rgba(244,239,230,.75);line-height:1.75;">The more I reflected on it, the more I realised the answer touched everything: identity, direction, intention, and the way I related to my own work. Over the years, that same question appeared again and again in conversations with other photographers &mdash; many were not struggling because of technique, but because they were unsure what truly mattered to them. Beyond Frame grew from those conversations.</p>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-header reveal">
      <p class="eyebrow">Why I Created Beyond Frame</p>
      <h2>Because the strongest work begins long before the camera is picked up.</h2>
      <p>Many photographers learn the tools, improve their images, and still feel stuck &mdash; not because they lack skill, but because they are unsure what they truly want to say. I created this program to go deeper than technical learning, and gradually translate what matters to you into stronger, more personal work.</p>
    </div>
    <div class="grid grid-4 reveal reveal-delay-1">
      <div><span class="pillar-num" style="font-size:1.6rem;">01</span><h3 style="font-size:1.1rem;margin:10px 0;">Start From Within</h3><p style="color:var(--ink-soft);font-size:.9rem;line-height:1.6;">We begin with the deeper layer &mdash; your story, your experiences, your concerns. Clarity comes first.</p></div>
      <div><span class="pillar-num" style="font-size:1.6rem;">02</span><h3 style="font-size:1.1rem;margin:10px 0;">Create With Purpose</h3><p style="color:var(--ink-soft);font-size:.9rem;line-height:1.6;">We develop your ideas into images that carry meaning and reflect who you are.</p></div>
      <div><span class="pillar-num" style="font-size:1.6rem;">03</span><h3 style="font-size:1.1rem;margin:10px 0;">Present With Confidence</h3><p style="color:var(--ink-soft);font-size:.9rem;line-height:1.6;">We build a portfolio and a way of presenting your work that is honest, clear, and professional.</p></div>
      <div><span class="pillar-num" style="font-size:1.6rem;">04</span><h3 style="font-size:1.1rem;margin:10px 0;">Step Into the Real World</h3><p style="color:var(--ink-soft);font-size:.9rem;line-height:1.6;">We explore opportunities, build connections, and position your work with intention.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Background</p>
      <h2>Shaped by curiosity, discipline, and experience.</h2>
      <div style="margin-top:32px;">
        <div class="contact-info-item" style="border-top:none;padding-top:0;"><div><h4>Education</h4><p style="font-family:var(--sans);color:var(--ink-soft);font-size:.95rem;">Studied Photography at the Royal Academy of Art, The Hague, Netherlands.</p></div></div>
        <div class="contact-info-item"><div><h4>Recognition</h4><p style="font-family:var(--sans);color:var(--ink-soft);font-size:.95rem;">Work exhibited and recognised through international platforms, exhibitions, and photography awards.</p></div></div>
        <div class="contact-info-item"><div><h4>Experience</h4><p style="font-family:var(--sans);color:var(--ink-soft);font-size:.95rem;">Long-term work in portrait and documentary photography across different people, cultures, and environments.</p></div></div>
        <div class="contact-info-item"><div><h4>Teaching</h4><p style="font-family:var(--sans);color:var(--ink-soft);font-size:.95rem;">Working with photographers through feedback, direction, and long-term development.</p></div></div>
      </div>
      <a href="https://hossein.art" target="_blank" rel="noopener" class="btn btn-outline" style="margin-top:20px;">View My Photography Work &nbsp;&#8599;</a>
    </div>
    <div class="split-media media-frame reveal reveal-delay-1">
      <img src="/assets/images/about/Hossein_Mentor.webp" alt="Hossein Fardinfard mentoring a photographer">
    </div>
  </div>
</section>

<section class="section bg-cream-soft">
  <div class="container">
    <div class="section-header reveal"><p class="eyebrow">Selected Works</p><h2>A glimpse of the personal projects behind the mentorship.</h2></div>
    <div class="grid grid-4 reveal reveal-delay-1">
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/about/selected_works_blackout.webp" alt="Blackout — selected work"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/about/selected_works_gamechanger.webp" alt="Gamechanger — selected work"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/about/selected_works_luna.webp" alt="Luna — selected work"></div>
      <div class="media-frame" style="aspect-ratio:3/4;"><img src="/assets/images/about/selected_works_seclusion.webp" alt="Seclusion — selected work"></div>
    </div>
  </div>
</section>

<section class="quote-block">
  <div class="container reveal statement text-center center-col">
    <p>&ldquo;I believe good photography begins with understanding yourself. <em>My role is not to tell you who to become. It is to help you uncover what is already there.</em>&rdquo;</p>
  </div>
</section>

<section class="cta-band bg-ink">
  <div class="container reveal">
    <p class="eyebrow" style="color:var(--clay-tint);">Work With Me</p>
    <h2 style="color:var(--paper);">Ready to see what your program would look like?</h2>
    <div class="cta-actions"><a href="/booking.html" class="btn btn-primary">Book a Direction Session</a><a href="/programs.html" class="btn btn-outline-light">Explore Programs</a></div>
  </div>
</section>
'''
)

# ---- TESTIMONIALS ----
page("testimonials.html",
  "Testimonials — Beyond Frame",
  "Beyond Frame is a private photography program by Hossein Fardinfard focused on mentorship, image-making, creative direction, and portfolio development.",
  "testimonials.html",
  '''
<section class="page-hero dark">
  <div class="container reveal">
    <p class="eyebrow">Testimonials</p>
    <h1 class="page-hero-title">Reflections From the Journey</h1>
    <p class="lead">Words from photographers and participants who have been part of the Beyond Frame mentorship.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2 reveal">

    <div class="testi-card">
      <div class="testi-avatar"><img src="/assets/images/testimonials/Teona.jpg" alt="Teona Machavariani"></div>
      <div class="testi-name">Teona Machavariani</div>
      <div class="testi-text">
        <p>Working with Hossein requires a certain kind of honesty. Not because he asks for it, but because sooner or later you realise that photography can only take you as far as you are willing to go yourself.</p>
        <p>Hossein has a rare ability to direct attention toward what is usually left unexplored. In that sense, the work is not just about learning how to make better images &mdash; it is about seeing yourself more clearly. An experience that continues to shape the way I work.</p>
      </div>
    </div>

    <div class="testi-card">
      <div class="testi-avatar">NC</div>
      <div class="testi-name">Nathan Collins</div>
      <div class="testi-text">
        <p>Working with Hossein changed the way I think about photography. What stood out was that our conversations were rarely about cameras or technical settings &mdash; instead they focused on understanding why we photograph.</p>
        <p>The experience felt less like a photography course and more like a process of creative development. It helped me see photography not only as a medium for making images, but as a way of understanding myself and the world.</p>
      </div>
    </div>

    <div class="testi-card">
      <div class="testi-avatar"><img src="/assets/images/testimonials/Talal.jpg" alt="Talal Mansoor"></div>
      <div class="testi-name">Talal Mansoor</div>
      <div class="testi-text">
        <p>My session with Hossein was impactful right from the first day. He teaches in a way that no other photography course does: he first helps you find your inner artist.</p>
        <p>Technology will continue to evolve throughout our lives, but once you get to know the artist within yourself, it no longer matters what gear or medium you use &mdash; your work will always reflect your own voice.</p>
      </div>
    </div>

    <div class="testi-card">
      <div class="testi-avatar"><img src="/assets/images/testimonials/Zeyad.jpg" alt="Zeyad Bashir"></div>
      <div class="testi-name">Zeyad Bashir</div>
      <div class="testi-text">
        <p>After joining your sessions, I started looking at photography projects differently &mdash; instead of seeing photos as individual images, I began thinking of them as part of a larger visual project, with a story, concept, and purpose behind it.</p>
        <p>The discussions about careers, personal experiences, and real-world projects turned out to be just as valuable. Learning doesn&rsquo;t only come from camera settings.</p>
      </div>
    </div>

    <div class="testi-card" style="grid-column:1/-1;">
      <div class="testi-avatar"><img src="/assets/images/testimonials/Anita.jpg" alt="Anna Korotinska"></div>
      <div class="testi-name">Anna Korotinska</div>
      <div class="testi-text">
        <p>I really enjoyed Hossein&rsquo;s photography sessions because they were about discovering your own perspective and voice as a photographer. The atmosphere was always relaxed, friendly, and inspiring &mdash; Hossein was genuinely interested in helping each person explore their own style, passion, and ideas.</p>
        <p>I appreciated how he encouraged us to think beyond taking &ldquo;nice photos&rdquo; and focus on creating meaningful stories and personal projects, including printing our photographs and thinking about how images can be presented. The sessions felt like a space for creativity, reflection, and growth.</p>
      </div>
    </div>

  </div>
</section>

<section class="cta-band bg-cream-soft">
  <div class="container reveal">
    <p class="eyebrow">Your Story Could Be Next</p>
    <h2>Ready to see what your program would look like?</h2>
    <div class="cta-actions"><a href="/booking.html" class="btn btn-primary">Book a Direction Session</a></div>
  </div>
</section>
'''
)

# ---- CONTACT ----
page("contact.html",
  "Contact — Beyond Frame",
  "Get in touch with Beyond Frame for questions about photography programs, direction sessions, applications, or collaborations.",
  "contact.html",
  '''
<section class="page-hero dark">
  <div class="container reveal">
    <p class="eyebrow">Contact</p>
    <h1 class="page-hero-title">If You&rsquo;d Like to Talk</h1>
    <p class="lead">If you have a question about the programs, your work, or simply want to reach out, I&rsquo;d love to hear from you.</p>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <div class="contact-info-item" style="border-top:none;padding-top:0;">
        <div class="ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16v16H4z"/><path d="M4 6l8 7 8-7"/></svg></div>
        <div><h4>Email</h4><a href="mailto:hello@beyondframe.studio">hello@beyondframe.studio</a></div>
      </div>
      <div class="contact-info-item">
        <div class="ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 15.5c0 .5-.4 1-.9 1.1-1.3.3-3.9.6-6-1.5-2.1-2.1-1.8-4.7-1.5-6 .1-.5.6-.9 1.1-.9h1.8c.4 0 .8.3.9.7l.6 2c.1.4 0 .8-.3 1l-.9.8c.5 1.2 1.5 2.2 2.7 2.7l.8-.9c.3-.3.7-.4 1-.3l2 .6c.4.1.7.5.7.9V15.5z"/></svg></div>
        <div><h4>WhatsApp</h4><a href="https://wa.me/31655935251" target="_blank" rel="noopener">+31 6 55935251</a></div>
      </div>
      <div class="contact-info-item">
        <div class="ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></div>
        <div><h4>Instagram</h4><a href="https://www.instagram.com/hossein.foto" target="_blank" rel="noopener">&#64;hossein.foto</a></div>
      </div>
      <div class="contact-info-item">
        <div class="ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.2-9-10a5 5 0 0 1 9-4 5 5 0 0 1 9 4c-2 3.8-9 10-9 10z"/></svg></div>
        <div><h4>Based In</h4><span>Worldwide &middot; Sessions Online</span></div>
      </div>
    </div>

    <div class="reveal reveal-delay-1">
      <form id="contact-form" novalidate>
        <div class="form-row">
          <div class="form-field"><label for="name">Full Name *</label><input type="text" id="name" name="name" required></div>
          <div class="form-field"><label for="email">Email *</label><input type="email" id="email" name="email" required></div>
        </div>
        <div class="form-field"><label for="subject">Subject *</label><input type="text" id="subject" name="subject" required></div>
        <div class="form-field"><label for="message">Your Message *</label><textarea id="message" name="message" required></textarea></div>
        <div class="form-field" style="position:absolute;left:-9999px;" aria-hidden="true"><label for="company">Company</label><input type="text" id="company" name="company" tabindex="-1" autocomplete="off"></div>
        <button type="submit" class="btn btn-primary">Send Message</button>
        <div id="form-status" class="form-status"></div>
        <p class="form-note">Messages are sent directly to hello&#64;beyondframe.studio. For booking a Direction Session, use the <a href="/booking.html" style="text-decoration:underline;">booking page</a> instead.</p>
      </form>
    </div>
  </div>
</section>
'''
)

# ---- LEGAL: TERMS ----
page("terms.html",
  "Terms & Conditions — Beyond Frame",
  "Read the terms and conditions for using Beyond Frame, including program participation, payments, bookings, and website usage.",
  "terms.html",
  '''
<section class="page-hero dark section-sm" style="padding-top:180px;">
  <div class="container reveal"><p class="eyebrow">Legal</p><h1 class="page-hero-title" style="font-size:2.6rem;">Terms &amp; Conditions</h1>
  <p class="lead">By accessing this website, submitting an inquiry, booking a session, or purchasing a service, you agree to the terms below.</p></div>
</section>
<section class="section">
  <div class="container legal-body reveal">
    <h2><span class="legal-num">01&nbsp;</span> About the Platform</h2>
    <p>Beyond Frame is a photography mentorship and creative guidance platform founded by Hossein Fardinfard. Services may include:</p>
    <ul><li>Private one-to-one mentorship sessions</li><li>Portfolio reviews</li><li>Direction Sessions</li><li>Educational and creative guidance</li><li>Development and strategy support</li></ul>

    <h2><span class="legal-num">02&nbsp;</span> Eligibility</h2>
    <p>Services are intended for individuals capable of making informed decisions. If a participant is under the legal age in their country, parental or guardian consent is required.</p>

    <h2><span class="legal-num">03&nbsp;</span> Nature of Services</h2>
    <p>Beyond Frame provides educational mentorship, creative guidance, feedback, and strategic support. These services are not therapy, legal advice, financial advice, immigration advice, or guaranteed career placement. Mentorship can support clarity, development, and progress, but results depend on each participant&rsquo;s effort, consistency, openness, and real-world conditions.</p>

    <h2><span class="legal-num">04&nbsp;</span> Booking &amp; Payment</h2>
    <p>Direction Sessions must be paid in advance. Mentorship programs follow the payment terms stated in the written proposal. A booking is confirmed only when payment has been received, a session time has been scheduled, and confirmation has been sent. Beyond Frame reserves the right to decline or postpone bookings when necessary.</p>

    <h2><span class="legal-num">05&nbsp;</span> Scheduling &amp; Time Zones</h2>
    <p>Sessions are offered internationally and may involve different time zones, taking place through Google Meet, Zoom, or another agreed platform. Participants are responsible for attending sessions at the correct local time.</p>

    <h2><span class="legal-num">06&nbsp;</span> Rescheduling &amp; Late Arrival</h2>
    <p>If you need to reschedule, please provide at least 24 hours&rsquo; notice. Late arrival may result in a shorter session, depending on availability. Missed sessions without reasonable notice may be considered completed.</p>

    <h2><span class="legal-num">07&nbsp;</span> Participant Responsibility</h2>
    <p>The effectiveness of mentorship depends on active engagement. Participants are expected to attend sessions prepared, complete assignments where relevant, actively produce and develop work between sessions, reflect honestly, and apply feedback consistently. No specific outcomes &mdash; income, clients, exhibitions, or publications &mdash; are guaranteed.</p>

    <h2><span class="legal-num">08&nbsp;</span> Intellectual Property</h2>
    <p>Participants retain full ownership of their photographs and creative work. All teaching materials, frameworks, session methods, and written content provided by Beyond Frame remain the intellectual property of Beyond Frame unless stated otherwise, and may not be reproduced, shared, published, or resold without written permission.</p>

    <h2><span class="legal-num">09&nbsp;</span> Respectful Conduct</h2>
    <p>All communication must remain respectful and professional. Harassment, abusive behaviour, discrimination, or repeated disrespect may result in refusal, suspension, or termination of services.</p>

    <h2><span class="legal-num">10&nbsp;</span> Confidentiality</h2>
    <p>Personal conversations and shared work are treated with discretion and respect. Complete digital security cannot be guaranteed across all communication and file-sharing platforms.</p>

    <h2><span class="legal-num">11&nbsp;</span> Changes to Services</h2>
    <p>Prices, programs, formats, and website content may evolve over time. Confirmed bookings follow the terms in place at the time of purchase unless otherwise agreed in writing.</p>

    <h2><span class="legal-num">12&nbsp;</span> Contact</h2>
    <p>For questions regarding these terms: <a href="mailto:hello@beyondframe.studio" style="text-decoration:underline;">hello@beyondframe.studio</a></p>
    <p style="margin-top:24px;">Beyond Frame is operated by <strong>Orange Luna L.L.C-FZ</strong>, Dubai, UAE.</p>
  </div>
</section>
'''
)

# ---- LEGAL: PRIVACY ----
page("privacy.html",
  "Privacy Policy — Beyond Frame",
  "Read the Beyond Frame privacy policy and learn how personal information and submitted data are collected, stored, and protected.",
  "privacy.html",
  '''
<section class="page-hero dark section-sm" style="padding-top:180px;">
  <div class="container reveal"><p class="eyebrow">Legal</p><h1 class="page-hero-title" style="font-size:2.6rem;">Privacy Policy</h1>
  <p class="lead">Beyond Frame respects your privacy and handles personal information with care, minimal collection, and responsible use.</p></div>
</section>
<section class="section">
  <div class="container legal-body reveal">
    <h2><span class="legal-num">01&nbsp;</span> Information Collected</h2>
    <p>When you contact Beyond Frame, apply for mentorship, or book a service, you may voluntarily provide information such as:</p>
    <ul><li>Name</li><li>Email address</li><li>Country or time zone</li><li>Photography level or experience</li><li>Website, portfolio, or social media links</li><li>Messages, goals, or application details</li><li>Scheduling preferences</li></ul>
    <p>Only information relevant to communication and service delivery is collected.</p>

    <h2><span class="legal-num">02&nbsp;</span> How Information Is Used</h2>
    <p>Your information may be used to respond to inquiries, review mentorship applications, arrange bookings and sessions, deliver mentorship services, provide feedback or follow-up communication, improve the quality of services, and maintain reasonable business records.</p>

    <h2><span class="legal-num">03&nbsp;</span> No Sale of Personal Data</h2>
    <p>Your personal information is never sold or shared with third parties for advertising purposes.</p>

    <h2><span class="legal-num">04&nbsp;</span> Third-Party Tools</h2>
    <p>Beyond Frame may use trusted third-party tools to operate its services, including website contact forms, email providers, calendar or scheduling tools, video call platforms, and payment processors. These services may store limited information required for their function. Users are encouraged to review the privacy policies of these providers where relevant.</p>

    <h2><span class="legal-num">05&nbsp;</span> Submitted Images &amp; Portfolios</h2>
    <p>If you share photographs, portfolio links, or documents, they are used only for review, mentorship, or feedback. They are not published or shared publicly without your permission, and full ownership remains with you.</p>

    <h2><span class="legal-num">06&nbsp;</span> Email Communication</h2>
    <p>By contacting Beyond Frame or submitting a form, you consent to receiving communication related to your inquiry or mentorship. You may request to stop non-essential communication at any time.</p>

    <h2><span class="legal-num">07&nbsp;</span> Data Retention</h2>
    <p>Personal information is retained only for as long as reasonably necessary for communication, mentorship delivery, record-keeping, or legal and administrative purposes. Reasonable efforts are made to protect personal information, though no online system can guarantee absolute security.</p>

    <h2><span class="legal-num">08&nbsp;</span> Your Rights</h2>
    <p>Where applicable, you may request to access your personal data, correct inaccurate information, request deletion of stored data, or withdraw consent for future communication. Requests may be sent to <a href="mailto:hello@beyondframe.studio" style="text-decoration:underline;">hello@beyondframe.studio</a>.</p>

    <h2><span class="legal-num">09&nbsp;</span> Updates</h2>
    <p>This Privacy Policy may be updated from time to time to reflect changes in services or legal requirements.</p>

    <h2><span class="legal-num">10&nbsp;</span> Cookies</h2>
    <p>This website may use basic cookies or analytics tools to improve functionality and understand general website usage. No invasive tracking or advertising-based profiling is used.</p>
    <p style="margin-top:24px;">Beyond Frame is operated by <strong>Orange Luna L.L.C-FZ</strong>, Dubai, UAE.</p>
  </div>
</section>
'''
)

# ---- LEGAL: REFUND ----
page("refund.html",
  "Refund Policy — Beyond Frame",
  "Read the Beyond Frame refund policy for information regarding direction sessions, photography programs, cancellations, and payments.",
  "refund.html",
  '''
<section class="page-hero dark section-sm" style="padding-top:180px;">
  <div class="container reveal"><p class="eyebrow">Legal</p><h1 class="page-hero-title" style="font-size:2.6rem;">Refund Policy</h1>
  <p class="lead">Beyond Frame aims to maintain clear, fair, and respectful policies regarding bookings, payments, and refunds. By booking any service, you agree to the terms outlined below.</p></div>
</section>
<section class="section">
  <div class="container legal-body reveal">
    <h2><span class="legal-num">01&nbsp;</span> Direction Sessions</h2>
    <p>Direction Sessions are standalone, time-reserved appointments. Once a session is confirmed and scheduled, it is generally non-refundable. If sufficient notice is provided, rescheduling may be possible.</p>

    <h2><span class="legal-num">02&nbsp;</span> Mentorship Packages</h2>
    <p>For multi-session mentorship packages, specific terms are clarified before starting, including session structure and schedule, payment arrangement, duration, and pause or continuation options. Once a session has taken place, completed sessions are non-refundable. Refund requests for unused sessions may be considered on a case-by-case basis. Long periods of inactivity or non-response may result in closure of the mentorship process without refund.</p>

    <h2><span class="legal-num">03&nbsp;</span> Rescheduling</h2>
    <p>If you need to change a scheduled session, please provide at least 24 hours&rsquo; notice where possible. Reasonable flexibility may be offered depending on the situation.</p>

    <h2><span class="legal-num">04&nbsp;</span> Missed Sessions</h2>
    <p>If a participant does not attend a scheduled session without prior notice, the session may be considered completed and will not be refunded.</p>

    <h2><span class="legal-num">05&nbsp;</span> Exceptional Circumstances</h2>
    <p>Unexpected situations or emergencies are considered with fairness and discretion. Beyond Frame aims to approach unexpected situations with fairness, discretion, and reasonable flexibility.</p>

    <h2><span class="legal-num">06&nbsp;</span> No Guaranteed Outcomes</h2>
    <p>Mentorship provides guidance, structure, feedback, and support, but does not guarantee specific outcomes such as income, clients, exhibitions, publications, or career results. Refunds are therefore not based on subjective expectations or anticipated outcomes.</p>

    <h2><span class="legal-num">07&nbsp;</span> Contact</h2>
    <p>For questions related to bookings, payments, or refunds: <a href="mailto:hello@beyondframe.studio" style="text-decoration:underline;">hello@beyondframe.studio</a></p>
  </div>
</section>
'''
)

# ---- 404 ----
page("404.html",
  "Page Not Found — Beyond Frame",
  "The page you're looking for doesn't exist.",
  "404.html",
  '''
<section class="page-hero dark text-center" style="min-height:70vh;display:flex;align-items:center;justify-content:center;flex-direction:column;">
  <div class="container reveal">
    <p class="eyebrow">Lost Your Way?</p>
    <h1 class="page-hero-title" style="margin:16px auto;">Page Not Found</h1>
    <p class="lead center-col">The page you were looking for doesn&rsquo;t exist, or may have moved.</p>
    <div class="cta-actions" style="margin-top:32px;"><a href="/" class="btn btn-primary">Back to Home</a></div>
  </div>
</section>
'''
)

# ---- pages are appended below by subsequent edits ----

if __name__ == "__main__":
    for p in PAGES:
        write_page(*p)
    print(f"Built {len(PAGES)} pages.")
