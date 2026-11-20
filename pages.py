"""Page content for the Village Health Access site.

Content is taken from the previous villagehealthaccess.org. Goals are labelled as goals,
never as results. <span class="ph">...</span> marks a fact still to be confirmed or supplied.
"""

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="40" height="40" rx="11" fill="#1660d6"/>'
        '<path d="M8 19 20 9l12 10" fill="none" stroke="#7fb2ff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M17 18h6v4h4v6h-4v4h-6v-4h-4v-6h4z" fill="#ffffff"/></svg>')

NAV = [("about.html", "About"), ("programs.html", "Programs"), ("impact.html", "Impact"),
       ("partners.html", "Partners"), ("news.html", "News"), ("contact.html", "Contact")]


def icon(d):
    return (f'<span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg></span>')


I_PHONE = icon('<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/><path d="M12 7v6M9 10h6"/>')
I_PILL = icon('<path d="M10.5 3.5a5 5 0 0 1 7 7l-7 7a5 5 0 0 1-7-7z"/><path d="m7 10 7 7"/>')
I_GOV = icon('<path d="M3 21h18M5 21V10M19 21V10M9.5 21V10M14.5 21V10M2 10l10-7 10 7z"/>')
I_DROP = icon('<path d="M12 2.5S5 10 5 14.5a7 7 0 0 0 14 0C19 10 12 2.5 12 2.5z"/><path d="M9 15h6M12 12v6"/>')
I_HEART = icon('<path d="M20.5 8.5c0 5-8.5 11-8.5 11s-8.5-6-8.5-11A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 8.5 2.5z"/>')
I_HAND = icon('<path d="M3 13h3l4 3h5a2 2 0 0 0 0-4h-3"/><path d="M6 13v7H3M14 12l5-2a2 2 0 0 1 2 3l-7 5H10"/>')
I_USERS = icon('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18.5 20a6.5 6.5 0 0 0-3-5.5"/>')
I_SPARK = icon('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>')
I_SCALE = icon('<path d="M12 3v18M5 21h14M4 7h16"/><path d="m4 7-2.5 6a3 3 0 0 0 5 0zM20 7l-2.5 6a3 3 0 0 0 5 0z"/>')
I_MAIL = icon('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6 8.5 7 8.5-7"/>')
I_MIC = icon('<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>')

LANGS = ["French", "English", "Ewe", "Hausa", "Yoruba", "Twi", "Mooré", "Bambara", "and local dialects"]
LANG_CHIPS = "".join(f"<li>{l}</li>" for l in LANGS)


def copy_row(addr):
    return f'<div class="copy-row"><code>{addr}</code><button class="copy-btn" type="button" data-copy="{addr}">Copy</button></div>'


CTA = '''<section class="band cta"><div class="wrap"><div class="cta-inner">
  <div style="display:grid;gap:.8rem"><p class="eyebrow">Support us</p><h2>Help healthcare reach the villages clinics can't.</h2></div>
  <div class="actions" style="margin:0"><a class="btn btn-gold" href="donate.html">Donate</a><a class="btn btn-ghost" href="donate.html#grants">Grant opportunities</a></div>
</div></div></section>'''

GOALS = '''<div class="goals">
  <div class="goal"><b>10,000+</b><span>families reached</span></div>
  <div class="goal"><b>7</b><span>West African countries</span></div>
  <div class="goal"><b>14</b><span>languages of care</span></div>
  <div class="goal"><b>500+</b><span>partner clinics and pharmacies</span></div>
</div>'''

# ---------------------------------------------------------------- HOME
HOME = f'''
<section class="band hero"><div class="wrap hero-grid">
  <div>
    <p class="pill"><span class="pill-dot"></span>In partnership with Verakou</p>
    <h1>Healthcare for <span class="hl">every village.</span></h1>
    <p class="lead">Free telemedicine and essential medicines for underserved communities across West Africa, delivered over the phones people already use, in the languages they speak.</p>
    <div class="actions"><a class="btn btn-gold" href="donate.html">Support our mission</a><a class="btn btn-ghost" href="programs.html">See our programs</a></div>
    <ul class="trust">
      <li><b>Free</b> for patients</li>
      <li><b>WhatsApp</b> first</li>
      <li><b>Licensed</b> clinicians</li>
    </ul>
  </div>
  <div class="hero-visual">
    <div class="phone" role="img" aria-label="Illustration of a WhatsApp consultation">
      <div class="phone-notch"></div>
      <div class="chat">
        <div class="chat-head"><span class="dot">VHA</span><div><b>Village Health Access</b><span>online</span></div></div>
        <div class="msg out">Good morning. My daughter has had a fever since yesterday.<i>Patient · translated from Ewe</i></div>
        <div class="msg in">Thank you. How old is she, and has she been tested for malaria?<i>Community health worker</i></div>
        <div class="msg in">A licensed clinician will review her case today.<i>Care coordination</i></div>
      </div>
    </div>
    <div class="float float-a"><span class="float-ic ok">✓</span><div><b>Clinician assigned</b><small>Reviewing case</small></div></div>
    <div class="float float-b"><span class="float-ic rx">Rx</span><div><b>Medicine ready</b><small>Partner pharmacy</small></div></div>
    <p class="visual-note">Illustration of how a consultation works</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">How it works</p><h2>From a message to medicine, without the long walk.</h2></div>
  <ol class="steps">
    <li><h3>Reach out by WhatsApp</h3><p>Patients connect through WhatsApp and digital health platforms, in their own language. No clinic visit or travel is needed to start.</p></li>
    <li><h3>Get triaged and seen</h3><p>A multilingual triage protocol routes each case to a licensed clinician for diagnosis, treatment and follow-up.</p></li>
    <li><h3>Receive medicine</h3><p>Prescriptions are filled through our network of licensed partner pharmacies, at no cost to the patient.</p></li>
  </ol>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we do</p><h2>Four programs, one goal: healthcare people can reach.</h2></div>
  <div class="grid g4">
    <article class="card">{I_PHONE}<h3>Telemedicine Access</h3><p>Free and subsidized virtual consultations for orphans, refugees, rural farmers and the urban poor.</p><a class="more" href="programs.html#telemedicine">Learn more →</a></article>
    <article class="card">{I_PILL}<h3>Essential Medicines</h3><p>Prescriptions filled at no cost, with a focus on HIV, TB, malaria and maternal health.</p><a class="more" href="programs.html#medicines">Learn more →</a></article>
    <article class="card">{I_GOV}<h3>Government Integration</h3><p>Working with health ministries to formalize community health worker networks and share surveillance data.</p><a class="more" href="programs.html#government">Learn more →</a></article>
    <article class="card">{I_DROP}<h3>Cholera &amp; Vaccines</h3><p>Cholera response in Togo and last-mile vaccine delivery to communities with no health facility.</p><a class="more" href="programs.html#cholera">Learn more →</a></article>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:3rem;align-items:start">
    <div class="prose">
      <p class="eyebrow">Our mission</p>
      <h2>Care that doesn't depend on income, location or language.</h2>
      <p>We provide free, high-quality telemedicine and essential medicines to the most underserved communities in West Africa. We launched in Togo in 2026 and are building toward rural, refugee and urban-poor communities across the region.</p>
      <p><a href="about.html">Read our story →</a></p>
    </div>
    <div style="display:grid;gap:1rem">
      <p class="eyebrow">Our 2030 goals</p>
      {GOALS.replace('class="goals"', 'class="goals two"')}
      <p class="small muted">These are goals, not results. We publish progress on our <a href="impact.html">impact page</a>.</p>
    </div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head" style="grid-template-columns:1fr auto;max-width:none;align-items:end"><div style="display:grid;gap:.7rem"><p class="eyebrow">News</p><h2>Latest updates</h2></div><a class="more" style="font-weight:700" href="news.html">All updates →</a></div>
  <div class="grid g3">
    <article class="card post"><time datetime="2026-08">August 2026</time><h3>WHO calls for urgent scale-up of cholera vaccines across West Africa</h3><p>An emergency call as cholera cases rise in Togo, Benin and Nigeria.</p></article>
    <article class="card post"><time datetime="2026-07">July 2026</time><h3>Togo launches national community health worker program</h3><p>A Ministry of Health framework for community health workers, open to NGOs and digital platforms.</p></article>
    <article class="card post"><time datetime="2026-06">June 2026</time><h3>Telemedicine adoption rising across francophone Africa</h3><p>An ECOWAS report points to sharp growth in WhatsApp-based consultations.</p></article>
  </div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- ABOUT
ABOUT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Who we are</p>
  <h1>About Village Health Access</h1>
  <p class="lead">A humanitarian initiative, in partnership with Verakou, bringing quality healthcare to the most vulnerable communities in West Africa.</p>
</div></section>

<section class="section"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">Our story</p>
    <h2>Born from what we saw firsthand.</h2>
    <p>Donald Daglo founded Village Health Access after seeing patients in Togo turned away from clinics because they could not afford care or could not reach it.</p>
    <p>Families were choosing between food and medicine. People walked for hours to reach clinics that were closed or out of stock. Across Togo, Ghana, Benin and beyond, the gap in access to care is wide.</p>
    <p>Village Health Access closes that gap with telemedicine, a network of partner pharmacies and community health workers, reaching people where they already are.</p>
    <p class="small muted">West Africa, 2026 to present</p>
  </div>
  <div style="display:grid;gap:1.25rem;align-content:start">
    <div class="panel"><p class="eyebrow">Mission</p><p style="font-size:1.2rem">To provide free telemedicine and access to essential medicines for the most vulnerable communities in West Africa.</p></div>
    <div class="panel"><p class="eyebrow">Vision</p><p style="font-size:1.2rem">A world where geography and income never determine health outcomes.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Our values</p><h2>What guides our work</h2></div>
  <div class="grid g4">
    <div class="card">{I_SCALE}<h3>Equity</h3><p>Everyone deserves quality care, whatever their income, location or language.</p></div>
    <div class="card">{I_HEART}<h3>Compassion</h3><p>We treat every patient with dignity and respect.</p></div>
    <div class="card">{I_SPARK}<h3>Innovation</h3><p>WhatsApp triage and multilingual support built for low-connectivity areas.</p></div>
    <div class="card">{I_HAND}<h3>Accountability</h3><p>Monthly impact data, financial transparency and measurable outcomes.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Leadership</p><h2>Board of Directors</h2><p class="muted">We are recruiting board members. If you have the experience below, we'd like to hear from you.</p></div>
  <div class="grid g3">
    <div class="card"><div class="person"><span class="avatar">DD</span><div style="display:grid;gap:.3rem"><h3>Donald Daglo</h3><p class="small"><b>Founder &amp; Executive Director</b></p><p class="small">Also leads Klinova, the health technology platform that supports VHA's programs.</p></div></div></div>
    <div class="card"><div class="person"><span class="avatar open">+</span><div style="display:grid;gap:.3rem"><h3>Medical Advisory Board</h3><p class="small"><b>Recruiting</b></p><p class="small">Licensed clinicians and public health leaders from West Africa.</p></div></div></div>
    <div class="card"><div class="person"><span class="avatar open">+</span><div style="display:grid;gap:.3rem"><h3>Finance &amp; Governance</h3><p class="small"><b>Recruiting</b></p><p class="small">Nonprofit finance and 501(c)(3) governance experience.</p></div></div></div>
  </div>
  <p style="margin-top:1.5rem"><a class="btn btn-line" href="contact.html">Express interest in joining</a></p>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem;align-items:center">
  <div class="prose">
    <p class="eyebrow">How we're organized</p>
    <h2>In partnership with Verakou. Powered by Klinova.</h2>
    <p>Village Health Access works in partnership with Verakou. Our telemedicine service is powered by Klinova, built on the Kinara platform.</p>
  </div>
  <div style="display:grid;gap:1rem">
    <div class="panel"><p class="eyebrow">Partner</p><h2 class="h3">Verakou</h2><p class="muted">Village Health Access works in partnership with Verakou. <span class="ph">one or two sentences on Verakou and its website</span></p></div>
    <div class="panel"><p class="eyebrow">Technology</p><h2 class="h3">Powered by Klinova, built on the Kinara platform</h2><p class="muted">Klinova provides the technology behind our programs: a WhatsApp-based, multilingual triage and care coordination system designed for low-connectivity areas.</p><p><a href="https://klinova.co">Visit klinova.co</a></p></div>
  </div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- PROGRAMS
PROGRAMS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">What we do</p>
  <h1>Programs built for the communities that need them most.</h1>
  <p class="lead">Four programs that address distance, cost, disconnection and preventable disease.</p>
</div></section>

<section class="section"><div class="wrap">

  <article class="program" id="telemedicine">
    <div class="prose">
      {I_PHONE}
      <h2>Telemedicine Access</h2>
      <p>Free and subsidized virtual consultations for orphans, refugees, rural farmers and the urban poor.</p>
      <p>Patients connect by app or WhatsApp. A community health worker completes a structured, multilingual triage and escalates to a licensed clinician for diagnosis, treatment and follow-up.</p>
    </div>
    <div class="side">
      <div class="panel"><p class="eyebrow">Languages of care</p><p class="muted small">Our translation network is planned to cover 14 languages, including:</p><ul class="chips">{LANG_CHIPS}</ul></div>
      <div class="panel"><p class="eyebrow">Where</p><p>Launched in Togo in 2026, expanding to Ghana, Benin and beyond, with a goal of 7 countries by 2030.</p></div>
    </div>
  </article>

  <article class="program" id="medicines">
    <div class="prose">
      {I_PILL}
      <h2>Essential Medicines</h2>
      <p>Prescriptions from telemedicine consultations are filled at no cost to the patient.</p>
      <p>We work through licensed pharmacies and government supply chains using WHO-prequalified medicines, with cold-chain handling for temperature-sensitive drugs through regional distributors.</p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">Focus areas</p>
      <ul class="list"><li>HIV antiretroviral treatment</li><li>Tuberculosis care</li><li>Malaria prevention and treatment</li><li>Maternal and newborn health</li><li>Childhood immunization support</li></ul>
    </div></div>
  </article>

  <article class="program" id="government">
    <div class="prose">
      {I_GOV}
      <h2>Government Integration</h2>
      <p>We aim to formalize community health worker networks with West African health ministries, share surveillance data and integrate telemedicine protocols into public health systems.</p>
      <p>We are in active conversations with health authorities in Togo, Ghana, Benin and Nigeria. No agreements have been signed yet.</p>
      <p><a class="btn btn-line" href="impact.html">View our impact data</a></p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">What we will share with ministries</p>
      <ul class="list"><li>Anonymized disease surveillance data</li><li>Community health worker coverage maps</li><li>Medicine supply status reports</li><li>Outbreak early-warning indicators</li><li>Consultation volume by region</li></ul>
    </div></div>
  </article>

  <article class="program" id="cholera">
    <div class="prose">
      {I_DROP}
      <h2>Combating Cholera &amp; Delivering Vaccines</h2>
      <p>Our cholera response in Togo combines oral rehydration, sanitation education and rapid deployment of community health workers.</p>
      <p>We deliver vaccines to the last mile, including nomadic groups, refugee camps and villages with no health facility. Outbreak data is logged on our platform for reporting to health authorities.</p>
    </div>
    <div class="side"><div class="panel"><p class="eyebrow">Vaccination programs</p>
      <ul class="list"><li>Cholera</li><li>Meningitis</li><li>Yellow fever</li><li>Routine childhood immunizations</li></ul>
    </div></div>
  </article>

</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Get involved</p><h2>There's a place for you in this work.</h2></div>
  <div class="grid g3">
    <div class="card">{I_HAND}<h3>Partner with us</h3><p>Clinics, pharmacies, NGOs and health agencies can join our referral and supply network.</p><a class="more" href="partners.html">Apply to partner →</a></div>
    <div class="card">{I_HEART}<h3>Donate</h3><p>Fund consultations, medicines and community health workers.</p><a class="more" href="donate.html">Support the mission →</a></div>
    <div class="card">{I_USERS}<h3>Volunteer</h3><p>We welcome licensed clinicians, translators, data analysts and public health professionals.</p><a class="more" href="contact.html">Get in touch →</a></div>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- IMPACT
ROADMAP = [
    ("live", "Togo", "Active", "Launched 2026. Our first and currently only active country."),
    ("", "Ghana", "Planned", "Next expansion country."),
    ("", "Benin", "Planned", "Next expansion country."),
    ("", "Nigeria", "Planned", "In conversation with health authorities."),
    ("", "Burkina Faso", "2028", "Expansion roadmap."),
    ("", "Côte d'Ivoire", "2028", "Expansion roadmap."),
    ("", "Senegal", "2029", "Expansion roadmap."),
]
ROADMAP_HTML = "".join(
    f'<li class="{c}"><div class="row"><h3>{n}</h3><span class="tag{" live" if c else ""}">{s}</span></div><p class="muted small">{d}</p></li>'
    for c, n, s, d in ROADMAP)

DISEASE = [("Fever / malaria", 34), ("Respiratory", 22), ("Digestive", 18), ("Maternal health", 12), ("Other", 14)]
BARS = "".join(
    f'<div class="bar"><span>{n}</span><div class="bar-track"><div class="bar-fill" style="width:{v / 34 * 100:.0f}%"></div></div><b>{v}%</b></div>'
    for n, v in DISEASE)

IMPACT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Measuring what matters</p>
  <h1>Our impact, reported honestly.</h1>
  <p class="lead">We are a young initiative. Here is where we are today, where we're going, and how we'll report progress each month.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">2030 goals</p><h2>What we're working toward</h2></div>
  <div class="goals">
    <div class="goal"><b>10,000+</b><span>consultations</span></div>
    <div class="goal"><b>12,000+</b><span>medicine packages</span></div>
    <div class="goal"><b>500+</b><span>partner clinics</span></div>
    <div class="goal"><b>14</b><span>languages</span></div>
  </div>
  <div class="panel" style="margin-top:1.25rem"><p class="eyebrow">Results to date</p><p>Consultations completed: <span class="ph">number and date</span> · Medicine packages delivered: <span class="ph">number and date</span> · Families served: <span class="ph">number and date</span></p></div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div>
    <div class="section-head"><p class="eyebrow">Where we work</p><h2>Country roadmap</h2></div>
    <ol class="roadmap">{ROADMAP_HTML}</ol>
  </div>
  <div>
    <div class="section-head"><p class="eyebrow">Consultations</p><h2>What patients come to us for</h2></div>
    <div class="panel"><div class="bars">{BARS}</div>
    <p class="small muted">Share of consultations by category. Period covered: <span class="ph">dates and number of consultations</span>.</p></div>
    <p class="muted" style="margin-top:1rem">Fever and malaria are the most common reasons people reach out, followed by respiratory illness. Maternal health consultations are a growing share.</p>
  </div>
</div></section>

<section class="section"><div class="wrap grid g2" style="gap:2rem">
  <div class="panel"><p class="eyebrow">Data transparency</p><h3>Updated monthly, always anonymized</h3><p class="muted">Impact data is updated monthly. Patient data is anonymized and never shared publicly. <a href="privacy.html">Read our privacy commitments</a>.</p></div>
  <div class="panel" id="annual-report"><p class="eyebrow">Annual report</p><h3>2026 Annual Report</h3><p class="muted">Our first annual report will be published here. <span class="ph">publication date or PDF link</span></p></div>
</div></section>
{CTA}
'''

# ---------------------------------------------------------------- PARTNERS
PARTNERS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Building our network</p>
  <h1>Partner with Village Health Access</h1>
  <p class="lead">We are building a network of clinics, pharmacies, NGOs and health agencies so that a WhatsApp message can turn into real care.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="grid g2" style="margin-bottom:2.5rem">
    <div class="panel"><p class="eyebrow">Partner</p><h2 class="h3">Verakou</h2><p class="muted">Village Health Access works in partnership with Verakou. <span class="ph">short description of Verakou</span></p></div>
    <div class="panel"><p class="eyebrow">Technology</p><h2 class="h3">Powered by Klinova, built on the Kinara platform</h2><p class="muted">Klinova provides the WhatsApp-based triage and care coordination technology our programs run on.</p></div>
  </div>
  <div class="section-head"><p class="eyebrow">Who we work with</p><h2>Partnerships we're building</h2></div>
  <div class="grid g4">
    <div class="card">{I_HEART}<h3>Clinics &amp; health facilities</h3><p>Receive referrals and support follow-up care.</p></div>
    <div class="card">{I_PILL}<h3>Pharmacies &amp; distributors</h3><p>Fill prescriptions and join our medicine supply coordination.</p></div>
    <div class="card">{I_USERS}<h3>NGOs &amp; civil society</h3><p>Extend reach into refugee, rural and urban-poor communities.</p></div>
    <div class="card">{I_GOV}<h3>Government health agencies</h3><p>We're in conversation with health authorities in Togo, Ghana, Benin and Nigeria.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">What partners get</p>
    <h2>Become a partner</h2>
    <ul class="list"><li>Access to our patient referral network</li><li>Medicine supply coordination</li><li>Training</li><li>Community health worker support</li></ul>
    <p>Prefer email? Write to us directly.</p>
    {copy_row("partners@villagehealthaccess.org")}
  </div>
  <div class="panel">
    <form data-mailto="partners@villagehealthaccess.org" data-subject="Partnership request">
      <div class="field"><label for="p-org">Organization name <span class="req">*</span></label><input id="p-org" name="organization" required></div>
      <div class="field"><label for="p-country">Country <span class="req">*</span></label><input id="p-country" name="country" required></div>
      <div class="field"><label for="p-email">Contact email <span class="req">*</span></label><input id="p-email" name="email" type="email" required></div>
      <div class="field"><label for="p-type">Type of partnership</label>
        <select id="p-type" name="partnership_type"><option>Clinic / healthcare facility</option><option>Pharmacy / medicine distributor</option><option>NGO / civil society</option><option>Government health agency</option><option>Community health worker program</option><option>Other</option></select></div>
      <div class="field"><label for="p-msg">Tell us about your organization</label><textarea id="p-msg" name="message"></textarea></div>
      <button class="btn btn-gold" type="submit">Submit partnership request</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- DONATE
DONATE = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Support our work</p>
  <h1>Fund healthcare for the unreachable.</h1>
  <p class="lead">Every gift goes to direct program delivery: consultations, medicines and community health workers.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What your gift does</p><h2>The impact of your donation</h2></div>
  <div class="amounts">
    <div class="card amount"><b>$25</b><h3>One consultation</h3><p>A telemedicine consultation with a licensed clinician.</p></div>
    <div class="card amount"><b>$100</b><h3>A month of medicine for a child</h3><p>Malaria or TB treatment, or nutritional supplements.</p></div>
    <div class="card amount"><b>$500</b><h3>A community health program</h3><p>One community health worker serving a remote village for a month.</p></div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">How to give today</p>
    <h2>Make a donation</h2>
    <p>Our 501(c)(3) application is pending, and secure online giving will open once it is approved. Until then, email us and we will arrange your donation directly and send you a receipt.</p>
    {copy_row("contact@villagehealthaccess.org")}
    <p class="small muted">Tax deductibility depends on our 501(c)(3) approval. Please consult your tax advisor.</p>
  </div>
  <div class="panel amount-picker">
    <p class="eyebrow">Choose an amount</p>
    <div class="actions" style="margin:0">
      <button class="btn btn-line" type="button" data-amount="25" aria-pressed="false">$25</button>
      <button class="btn btn-line" type="button" data-amount="50" aria-pressed="false">$50</button>
      <button class="btn btn-line" type="button" data-amount="100" aria-pressed="true">$100</button>
      <button class="btn btn-line" type="button" data-amount="250" aria-pressed="false">$250</button>
    </div>
    <form data-mailto="contact@villagehealthaccess.org" data-subject="Donation pledge">
      <div class="field"><label for="d-name">Your name</label><input id="d-name" name="name" required></div>
      <div class="field"><label for="d-amount">Amount (USD)</label><input id="d-amount" name="amount" inputmode="decimal" placeholder="Or enter your own amount"></div>
      <button class="btn btn-gold" type="submit">Pledge <span data-amount-out>$100</span> by email</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
</div></section>

<section class="section" id="grants"><div class="wrap grid g2" style="gap:3rem">
  <div class="prose">
    <p class="eyebrow">Institutional funding</p>
    <h2>Grant opportunities</h2>
    <p>We welcome proposals from foundations, bilateral and multilateral donors and impact investors, for both restricted and unrestricted funding.</p>
    <p>Email us with the subject "Grant Information Request".</p>
    {copy_row("contact@villagehealthaccess.org")}
  </div>
  <div class="panel"><p class="eyebrow">Restricted funding areas</p>
    <ul class="list"><li>Telemedicine infrastructure expansion</li><li>Community health worker training and deployment</li><li>Essential medicine supply chain</li><li>Maternal and child health</li><li>Disease surveillance and public health data</li><li>Multi-country replication</li></ul>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div>
    <div class="section-head"><p class="eyebrow">Thank you</p><h2>Current supporters</h2></div>
    <div class="grid" style="gap:.8rem">
      <div class="panel"><h3>Verakou</h3><p class="muted small">Partner</p></div>
      <div class="panel"><h3>Klinova</h3><p class="muted small">In-kind technology partner</p></div>
      <div class="panel"><h3>Founding Friends Fund</h3><p class="muted small">Individual donors</p></div>
      <div class="panel"><h3>West Health Foundation</h3><p class="muted small">Early-stage funder</p></div>
    </div>
  </div>
  <div>
    <div class="section-head"><p class="eyebrow">Financial transparency</p><h2>Where the money goes</h2></div>
    <div class="goals" style="grid-template-columns:repeat(2,minmax(0,1fr))">
      <div class="goal"><b>85%+</b><span>to programs (target)</span></div>
      <div class="goal"><b>&lt;15%</b><span>overhead (target)</span></div>
    </div>
    <p class="muted" style="margin-top:1rem">We publish financial reporting, and full financial statements are available on request.</p>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- NEWS
NEWS = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Updates</p>
  <h1>News &amp; updates</h1>
  <p class="lead">Regional health news, disease alerts, policy and technology that shape our work, plus updates from the field.</p>
</div></section>

<section class="section"><div class="wrap" style="max-width:860px">
  <div style="display:grid;gap:1.25rem">
    <article class="card post"><time datetime="2026-08">August 2026 · Disease alert</time><h2 style="font-size:1.6rem">WHO calls for urgent scale-up of cholera vaccines across West Africa</h2><p>The World Health Organization issued an emergency call to scale up cholera vaccination as cases rise in Togo, Benin and Nigeria. Cholera response is one of our four programs.</p><a class="more" href="programs.html#cholera">Our cholera &amp; vaccine program →</a></article>
    <article class="card post"><time datetime="2026-07">July 2026 · Policy</time><h2 style="font-size:1.6rem">Togo launches national community health worker program</h2><p>Togo's Ministry of Health introduced a national framework for community health workers that is open to NGOs and digital health platforms.</p><a class="more" href="programs.html#government">Our government integration work →</a></article>
    <article class="card post"><time datetime="2026-06">June 2026 · Technology</time><h2 style="font-size:1.6rem">Telemedicine adoption rising across francophone Africa</h2><p>An ECOWAS report describes a 340% rise in WhatsApp-based consultations across francophone Africa.</p><a class="more" href="programs.html#telemedicine">Our telemedicine program →</a></article>
  </div>
  <div class="panel" style="margin-top:2.5rem"><p class="eyebrow">Stay informed</p><h3>Get monthly impact updates</h3><p class="muted">Program milestones, field stories and policy news, once a month. Sign up in the footer below.</p></div>
</div></section>
'''

# ---------------------------------------------------------------- CONTACT
CONTACT = f'''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Reach us</p>
  <h1>Get in touch.</h1>
  <p class="lead">Whether you want to partner, donate, volunteer or learn more, we reply within 2 business days.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Find the right inbox</p><h2>Email us directly</h2></div>
  <div class="grid g3">
    <div class="card">{I_MAIL}<h3>General inquiries</h3><p>Questions, donations and volunteering.</p>{copy_row("contact@villagehealthaccess.org")}</div>
    <div class="card">{I_HAND}<h3>Partnerships</h3><p>Clinics, pharmacies, NGOs and government.</p>{copy_row("partners@villagehealthaccess.org")}</div>
    <div class="card">{I_MIC}<h3>Media</h3><p>Press and interview requests.</p>{copy_row("media@villagehealthaccess.org")}</div>
  </div>
</div></section>

<section class="section section-alt"><div class="wrap grid g2" style="gap:3rem">
  <div class="panel">
    <h2 style="font-size:1.6rem">Send us a message</h2>
    <form data-mailto="contact@villagehealthaccess.org" data-subject="Website message">
      <div class="field"><label for="c-name">Full name <span class="req">*</span></label><input id="c-name" name="name" required></div>
      <div class="field"><label for="c-email">Email <span class="req">*</span></label><input id="c-email" name="email" type="email" required></div>
      <div class="field"><label for="c-subject">Subject</label><select id="c-subject" name="subject"><option>General</option><option>Partnership</option><option>Donation</option><option>Volunteering</option><option>Media</option><option>Other</option></select></div>
      <div class="field"><label for="c-msg">Message <span class="req">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
      <button class="btn btn-gold" type="submit">Send message</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
  </div>
  <div style="display:grid;gap:1.25rem;align-content:start">
    <div class="prose"><p class="eyebrow">Where we are</p><h2 style="font-size:1.6rem">Distributed across West Africa</h2><p>We don't have a central office. Our team works where our patients are. We are active in Togo and building toward Ghana, Benin, Nigeria, Burkina Faso, Côte d'Ivoire and Senegal.</p></div>
    <div class="panel"><p class="eyebrow">Follow our work</p>
      <ul class="list" style="list-style:none;padding:0">
        <li><a href="https://x.com/villagehealthacc">X (Twitter) · @villagehealthacc</a></li>
        <li><a href="https://linkedin.com/company/village-health-access">LinkedIn · Village Health Access</a></li>
        <li>WhatsApp · <span class="ph">public WhatsApp number</span></li>
      </ul>
    </div>
  </div>
</div></section>
'''

# ---------------------------------------------------------------- PRIVACY
PRIVACY = '''
<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>Our privacy commitments</h1>
</div></section>
<section class="section"><div class="wrap prose">
  <p>Patient data is anonymized before it is used in any reporting, and it is never shared publicly.</p>
  <p>Data we share with health authorities, such as disease surveillance figures, is anonymized and aggregated.</p>
  <p><span class="ph">full privacy policy, reviewed by counsel</span></p>
  <p>Questions about your data? Email contact@villagehealthaccess.org.</p>
</div></section>
'''

PAGES = {
    "home": ("index.html", "Home", HOME),
    "about": ("about.html", "About", ABOUT),
    "programs": ("programs.html", "Programs", PROGRAMS),
    "impact": ("impact.html", "Impact", IMPACT),
    "partners": ("partners.html", "Partners", PARTNERS),
    "donate": ("donate.html", "Donate", DONATE),
    "news": ("news.html", "News", NEWS),
    "contact": ("contact.html", "Contact", CONTACT),
    "privacy": ("privacy.html", "Privacy", PRIVACY),
}
