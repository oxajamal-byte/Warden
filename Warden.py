import re
import urllib.parse
import datetime
import time
import random

print("=" * 70)
print("🛡️" + " " * 8 + "ADVANCED SECURITY THREAT DETECTOR" + " " * 8 + "🛡️")
print("=" * 70)

class AdvancedThreatDetector:
    def __init__(self):

        self.known_malicious_sites = {
            'aniwatchtv.to':   {'risk': 'HIGH',     'type': 'Piracy Streaming',  'threats': ['Copyright infringement', 'Malware risk', 'Unverified ads']},
            'movies2watch.tv': {'risk': 'HIGH',     'type': 'Piracy Streaming',  'threats': ['Illegal content', 'Malware distribution', 'Phishing ads']},
            'fmoviesz.to':     {'risk': 'HIGH',     'type': 'Piracy Streaming',  'threats': ['Copyright violation', 'Security risks', 'Malicious ads']},
            'soap2day.to':     {'risk': 'CRITICAL', 'type': 'Piracy Streaming',  'threats': ['Malware hosting', 'Illegal streaming', 'Data theft risk']},
            '123movies':       {'risk': 'HIGH',     'type': 'Piracy Streaming',  'threats': ['Copyright infringement', 'Malware', 'Phishing']},
            'scam-click':      {'risk': 'CRITICAL', 'type': 'Scam / Click-fraud','threats': ['Designed to steal clicks/money', 'Fake rewards', 'Credential theft']},
            'free-prize':      {'risk': 'CRITICAL', 'type': 'Scam',              'threats': ['Fake prize scam', 'Personal info harvesting']},
            'login-verify':    {'risk': 'CRITICAL', 'type': 'Phishing',          'threats': ['Credential phishing', 'Identity theft']},
            'account-update':  {'risk': 'CRITICAL', 'type': 'Phishing',          'threats': ['Account takeover attempt']},
            'secure-banking':  {'risk': 'CRITICAL', 'type': 'Banking Phishing',  'threats': ['Banking credential theft']},
        }

        
        self.suspicious_keywords = {
            'login':          "The word 'login' in a domain is a classic phishing trick — real banks and services never put this in their web address.",
            'verify':         "Scammers use 'verify' to make you think your account needs urgent attention. Legitimate sites don't ask you to verify via a random link.",
            'secure':         "Ironically, scam sites love the word 'secure' to appear trustworthy — real secure sites don't need to advertise it in their URL.",
            'account':        "Having 'account' in the domain (not the path) is a red flag — attackers use it to mimic bank or service login pages.",
            'update':         "Fake 'update' pages are used to trick users into entering credentials or downloading malware.",
            'banking':        "A legitimate bank will never have 'banking' stuffed into a random domain. This is almost always a phishing site.",
            'password':       "No real website puts 'password' in its domain. This is almost certainly a credential-harvesting trap.",
            'signin':         "Same trick as 'login' — attackers create fake sign-in pages to steal your username and password.",
            'validation':     "Sites claiming to 'validate' your account via a link are trying to phish your credentials.",
            'authenticate':   "Real services don't ask you to authenticate through a suspicious third-party domain.",
            'confirm':        "'Confirm' pages are used in phishing emails to make you think you need to take urgent action.",
            'security':       "Scam sites put 'security' in their name to seem official. Real security alerts come from verified official domains.",
            'verification':   "A classic phishing signal — fake 'verification required' pages designed to steal your personal info.",
            'credential':     "No legitimate site uses the word 'credential' in its domain. This screams credential-theft operation.",
            'wallet':         "Crypto wallet phishing is very common — attackers build fake wallet sites to drain your funds.",
            'payment':        "Fake payment pages steal your card details. Always verify you're on the official site before paying.",
            'billing':        "Billing phishing tricks you into entering card or bank details on a fake page.",
            'invoice':        "Fake invoice sites are used to trick businesses into paying scammers or downloading malware.",
            'recover':        "Fake 'account recovery' pages are designed to make you hand over your real credentials.",
            'unlock':         "Scammers use 'unlock' to create fake urgency — claiming your account is locked to rush you into a bad decision.",
            'suspended':      "Fake 'your account is suspended' messages are a common phishing tactic to steal login details.",
            'limited':        "Claiming your account is 'limited' (as PayPal scams often do) is a major phishing red flag.",
            'actionrequired': "No real service embeds 'actionrequired' into a URL. This is designed to panic you into clicking.",
            'click':          "Domains with 'click' are often used for click-fraud, ad scams, or redirect-based phishing attacks.",
            'free':           "If a site's domain promises something 'free', it usually means you're the product — your data or device is at risk.",
            'prize':          "Fake prize pages are one of the oldest internet scams. Nobody is giving away prizes via a random link.",
            'winner':         "Fake winner notifications are used to harvest personal information. You didn't win anything.",
            'gift':           "Fake gift card or gift claim pages are phishing traps used to steal personal and financial details.",
            'reward':         "Fake reward pages claim you've earned something to lure you into giving personal information.",
            'urgent':         "The word 'urgent' in a domain is a psychological pressure tactic used by scammers.",
            'support':        "Fake support pages are used to impersonate tech companies and steal your credentials or money.",
            'helpdesk':       "Scammers use fake helpdesk pages to pretend to be Microsoft, Apple, or your bank.",
            'alert':          "Fake security alert pages try to scare you into calling a fake number or entering credentials.",
            'notice':         "Fake notice pages mimic official communications to trick you into handing over information.",
        }

        
        self.piracy_indicators = {
            'rip':          "Content 'rips' are illegal copies of movies, games or music. Sites hosting them are often full of malware.",
            'crack':        "Software cracks disable paid software illegally. They are one of the #1 ways malware is distributed.",
            'keygen':       "Key generators (keygens) for paid software are almost always bundled with trojans or ransomware.",
            'torrent':      "Torrent sites distribute copyrighted content illegally and often expose your device to malware.",
            'pirate':       "Piracy sites violate copyright law and frequently host malicious ads or infected downloads.",
            'freedownload': "Sites offering free downloads of paid content are a major malware distribution channel.",
            'serial':       "Sites giving away software serial keys are distributing stolen licenses and often malware too.",
            'patch':        "Unofficial software patches are frequently used to smuggle malware onto your computer.",
            'warez':        "'Warez' is a term for illegally distributed software — these sites are extremely high risk.",
            'cracked':      "Cracked software is pirated AND frequently infected with viruses, keyloggers, or ransomware.",
            'fullversion':  "Sites offering 'full versions' of paid software for free are piracy sites with high malware risk.",
            'nosteam':      "No-Steam patches are used to pirate Steam games. They are illegal and often contain malware.",
            'repack':       "Repacked software installers are often pirated and may include hidden malware.",
            'fitgirl':      "FitGirl repacks are pirated game versions. Impersonator sites often contain ransomware.",
            'skidrow':      "SKIDROW is a known piracy group. Sites using this name distribute illegal, potentially infected files.",
            'watchfree':    "Watch-free movie sites stream copyrighted content illegally and typically contain malicious ads.",
            'freemovies':   "Sites offering free movies are violating copyright and often serve malware through their ads.",
            'streamfree':   "Free streaming sites host illegal content and are notorious for harmful advertisements.",
            'putlocker':    "Putlocker is a known piracy streaming brand. Any site using this name is high risk.",
            'movie4k':      "4K movie piracy sites offer stolen content and carry serious malware and legal risks.",
        }

        
        self.high_risk_tlds = {
            '.to':    "The .to domain (Tonga) is popular with piracy and scam sites because it has minimal regulation.",
            '.ru':    "Russian .ru domains appear frequently in malware, phishing, and cybercrime infrastructure.",
            '.cn':    ".cn domains are sometimes used for international scam operations targeting Western users.",
            '.cc':    ".cc domains have very little oversight and are popular with spammers and scammers.",
            '.tk':    ".tk (Tokelau) domains are free and commonly abused for phishing and spam campaigns.",
            '.ml':    ".ml domains are free and regularly used for phishing and malware distribution.",
            '.ga':    ".ga domains are free and frequently appear in phishing kits.",
            '.cf':    ".cf is another free TLD exploited heavily by phishing operators.",
            '.xyz':   ".xyz domains are very cheap and often used for throwaway scam or spam sites.",
            '.top':   ".top is one of the most abused TLDs for phishing and scam websites.",
            '.club':  ".club domains appear frequently in spam and scam campaigns.",
            '.info':  ".info has a long history of being used for spam, scams, and low-quality content.",
            '.biz':   ".biz domains are frequently used in scam and phishing operations.",
            '.online': ".online is cheap to register and heavily used in phishing campaigns.",
            '.click':  ".click domains are a major red flag — primarily used for click-fraud and phishing.",
            '.link':   ".link domains are often used for redirect-based phishing and spam.",
            '.gq':    ".gq is a free TLD widely exploited for phishing and malware delivery.",
            '.pw':    ".pw (Palau) is commonly used for spam and phishing due to low cost.",
            '.ws':    ".ws is cheap and used in numerous scam and phishing operations.",
        }

       
        self.legitimate_brands = {
            'paypal':       ['paypal.com', 'paypal-business.com'],
            'microsoft':    ['microsoft.com', 'live.com', 'outlook.com', 'office.com', 'xbox.com'],
            'google':       ['google.com', 'gmail.com', 'youtube.com', 'googleapis.com'],
            'apple':        ['apple.com', 'icloud.com'],
            'amazon':       ['amazon.com', 'aws.amazon.com', 'amazon.co.uk'],
            'facebook':     ['facebook.com', 'fb.com', 'messenger.com'],
            'netflix':      ['netflix.com'],
            'steam':        ['store.steampowered.com', 'steampowered.com', 'steamcommunity.com'],
            'deepseek':     ['deepseek.com'],
            'github':       ['github.com', 'githubusercontent.com'],
            'twitter':      ['twitter.com', 'x.com'],
            'instagram':    ['instagram.com'],
            'tiktok':       ['tiktok.com'],
            'snapchat':     ['snapchat.com'],
            'discord':      ['discord.com', 'discordapp.com'],
            'spotify':      ['spotify.com'],
            'disney':       ['disneyplus.com', 'disney.com'],
            'hbo':          ['hbomax.com', 'max.com'],
            'hulu':         ['hulu.com'],
            'crunchyroll':  ['crunchyroll.com'],
            'binance':      ['binance.com'],
            'coinbase':     ['coinbase.com'],
            'robinhood':    ['robinhood.com'],
            'chase':        ['chase.com'],
            'wellsfargo':   ['wellsfargo.com'],
            'bankofamerica':['bankofamerica.com'],
            'irs':          ['irs.gov'],
            'linkedin':     ['linkedin.com'],
        }

        self.scam_patterns = [
            (r'scam',           "The word 'scam' literally appears in this domain — a massive red flag."),
            (r'phish',          "The word 'phish' appears in this domain — likely a test or actual phishing site."),
            (r'malware',        "'Malware' appears in the domain — treat this as dangerous."),
            (r'hack',           "'Hack' in the domain suggests illegal or malicious activity."),
            (r'virus',          "'Virus' in the domain is a serious warning sign."),
            (r'exploit',        "'Exploit' suggests this site may target software vulnerabilities."),
            (r'steal',          "'Steal' in the domain is an obvious danger signal."),
            (r'fake',           "'Fake' in the domain suggests impersonation or fraud."),
            (r'money-?back',    "Fake refund/money-back sites are used to steal payment information."),
            (r'click-?here',    "'Click-here' domains are used in phishing redirect chains."),
            (r'you-?won',       "Fake 'you won' pages are classic scam lures — you didn't win anything."),
            (r'claim-?now',     "Fake prize claim pages are used to harvest personal information."),
            (r'crypto-?gift',   "Crypto gift scams promise free cryptocurrency to steal wallet credentials."),
            (r'\d{4,}',         "A domain with many numbers in a row is often generated automatically by scam tools."),
        ]

        self.streaming_piracy_terms = [
            'aniwatch', 'movies2watch', 'fmovies', 'soap2day', '123movies',
            'putlocker', 'solarmovie', 'yts', 'eztv', 'rarbg', 'limetorrents',
            'kickasstorrents', 'piratebay', '1337x', 'torlock', 'gomovies',
            'lookmovie', 'primewire', 'watchsomuch', 'moviesda', 'tamilrockers',
        ]

   

    def show_welcome(self):
        welcome_messages = [
            "🚀 Welcome to your professional security analyzer!",
            "🔒 Your digital bodyguard is now active!",
            "🛡️  Threat detection system initialized!",
            "👁️  Suspicious activity detector online!",
            "💻 Cybersecurity assistant ready to serve!"
        ]
        print("\n" + random.choice(welcome_messages))
        print("\n" + "⭐" * 35)
        print("\n📋 I CAN ANALYZE:")
        print("   • Full URLs (https://example.com/page)")
        print("   • Malformed URLs (http//scam.com, hxxp://evil.com)")
        print("   • Website names (google, facebook, steamrip)")
        print("   • Application names (whatsapp, spotify, photoshop)")
        print("   • Suspicious links from emails or messages")
        print("\n🔍 I DETECT:")
        print("   ✅ Phishing & credential harvesting")
        print("   ✅ Brand impersonation")
        print("   ✅ Malformed / obfuscated links")
        print("   ✅ Scam & fraud domains")
        print("   ✅ Piracy & copyright sites")
        print("   ✅ Malware distribution sites")
        print("   ✅ Illegal streaming sites")
        print("   ✅ Suspicious TLDs & domain tricks")
        print("\n💡 TIP: Plain-English explanation for every red flag found!")
        print("⭐" * 35)
        print("\nInitializing detection systems", end="")
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print(" ✅ READY!\n")

    def normalize_input(self, raw):
        """Standardize input to a URL we can parse, flagging malformed inputs."""
        s = raw.strip()
        malformed_flags = []

        obfuscation_patterns = [
            (r'^hxxp://',       'hxxp://'),
            (r'^hxxps://',      'hxxps://'),
            (r'^http//',        'http//'),
            (r'^https//',       'https//'),
            (r'^http:\\\\',     'http:\\\\'),
            (r'^https:\\\\',    'https:\\\\'),
            (r'^http:(?!/)',     'http: without //'),
            (r'^https:(?!/)',    'https: without //'),
        ]
        for pattern, label in obfuscation_patterns:
            if re.match(pattern, s, re.IGNORECASE):
                malformed_flags.append(label)
                
                s = re.sub(pattern, 'https://', s, flags=re.IGNORECASE)


        if not s.startswith(('http://', 'https://')):
            if '.' in s and ' ' not in s:
                s = 'https://' + s
            else:
                s = 'https://' + s + '-check.com'

        return s, malformed_flags

    def extract_domain(self, url):
        try:
            if '://' in url:
                url = url.split('://', 1)[1]
            domain = url.split('/')[0].split(':')[0].lower()
            return domain
        except Exception:
            return url.lower()

    def get_tld(self, domain):
        parts = domain.split('.')
        return ('.' + parts[-1]) if len(parts) >= 2 else ''

    def check_known_malicious(self, domain):
        for site, info in self.known_malicious_sites.items():
            if site in domain:
                return info['risk'], info['type'], info['threats']
        return None, None, None


    def _add(self, findings, score, points, emoji, title, explanation):
        """Helper: append a structured finding."""
        findings.append({
            'points':      points,
            'emoji':       emoji,
            'title':       title,
            'explanation': explanation,
        })
        return score + points

    def analyze_structure(self, original_raw, url, domain, malformed_flags):
        """URL structure, scheme, and encoding checks."""
        findings = []
        score = 0

        for flag in malformed_flags:
            score = self._add(findings, score, 8, '🚨',
                f'MALFORMED URL SCHEME: "{flag}"',
                f'The link uses a broken or disguised format ("{flag}") instead of a normal '
                f'"https://". This is a common trick used in phishing emails so that security '
                f'filters don\'t catch the link, and to confuse victims into clicking without '
                f'realising it leads somewhere dangerous.')

       
        if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', domain):
            score = self._add(findings, score, 8, '🚨',
                'USES A RAW IP ADDRESS INSTEAD OF A REAL DOMAIN',
                'Legitimate websites always use a proper domain name (like google.com). '
                'When a link goes directly to an IP address (like 192.168.1.1), it almost '
                'always means the attacker is hiding a real domain. This is a classic '
                'phishing and malware delivery technique.')

  
        if '@' in url:
            score = self._add(findings, score, 8, '🚨',
                'USES @ SYMBOL TO DISGUISE THE REAL DESTINATION',
                'In a URL, everything before the @ symbol is ignored by your browser — the '
                'real destination is what comes after. Scammers use this to make a link look '
                'like it goes to "paypal.com@evil.com" when it actually goes to evil.com. '
                'Never trust a link containing @.')

        
        url_count = len(re.findall(r'https?://', url))
        if url_count > 1:
            score = self._add(findings, score, 7, '🚨',
                'CONTAINS A URL INSIDE ANOTHER URL (redirect chain)',
                'This link embeds a second URL inside it, which is a redirect trick. '
                'Attackers do this to pass through trusted link-shortening or email-tracking '
                'services before landing you on a malicious page.')

        if '%' in domain or '0x' in domain.lower():
            score = self._add(findings, score, 7, '🚨',
                'DOMAIN IS ENCODED / OBFUSCATED',
                'The domain uses percent-encoding (like %61%70%70%6C%65) or hex values to '
                'hide what the real address is. No legitimate website obscures its own name '
                'like this — this is an evasion technique used in phishing attacks.')

        suspicious_chars = re.findall(r'[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ]', domain)
        if suspicious_chars:
            score = self._add(findings, score, 7, '🚨',
                f'USES LOOKALIKE CHARACTERS: {suspicious_chars}',
                'The domain contains accented or special characters that look almost identical '
                'to normal letters (e.g. "pаypal.com" with a Cyrillic "а" instead of a Latin '
                '"a"). This is called a homoglyph attack — your eye sees "paypal" but your '
                'browser goes somewhere completely different.')


        if 'data:' in url or 'javascript:' in url.lower():
            score = self._add(findings, score, 10, '🚨',
                'DANGEROUS EMBEDDED PROTOCOL (data: / javascript:)',
                'This link uses a "data:" or "javascript:" URI, which can run malicious '
                'code directly in your browser without loading any website. This is a '
                'highly sophisticated attack technique — do not click this under any '
                'circumstances.')


        if url.startswith('http://') and not url.startswith('https://'):
            score = self._add(findings, score, 3, '⚠️',
                'NOT USING SECURE HTTPS',
                'This site uses plain HTTP, which means your connection is not encrypted. '
                'Any data you enter (passwords, card numbers) can be intercepted. All '
                'legitimate modern websites use HTTPS. This alone is not proof of a scam, '
                'but combined with other red flags it increases the risk.')

    
        subdomain_count = len(domain.split('.')) - 2
        if subdomain_count >= 3:
            score = self._add(findings, score, 4, '⚠️',
                f'UNUSUALLY DEEP SUBDOMAINS ({subdomain_count} levels)',
                f'This domain has {subdomain_count} subdomain levels (e.g. secure.login.verify.evil.com). '
                f'Scammers build deep subdomain chains to make the "safe-looking" part appear '
                f'first, hoping you won\'t read all the way to the actual root domain at the end.')

       
        if domain.count('-') >= 3:
            score = self._add(findings, score, 3, '⚠️',
                f'EXCESSIVE HYPHENS IN DOMAIN ({domain.count("-")} hyphens)',
                f'Legitimate websites rarely use more than one or two hyphens. Domains with '
                f'many hyphens (like secure-account-login-verify.com) are typically created '
                f'by scammers trying to string together trust-sounding words.')

       
        if len(domain) > 40:
            score = self._add(findings, score, 3, '⚠️',
                f'UNUSUALLY LONG DOMAIN NAME ({len(domain)} characters)',
                'Real company domains are short and memorable. Very long domain names are '
                'often generated automatically by phishing kits, or built to include a '
                'trusted brand name buried inside a long string of words.')

        return score, findings

    def analyze_domain_content(self, domain, original_raw):
        """Keyword, pattern, TLD, brand, and database checks."""
        findings = []
        score = 0
        domain_clean = domain.replace('-', '').replace('.', '')
        original_lower = original_raw.lower().strip()

       
        risk_level, site_type, threats = self.check_known_malicious(domain)
        if not risk_level:
            risk_level, site_type, threats = self.check_known_malicious(original_lower)
        if risk_level:
            pts = 20 if risk_level == 'CRITICAL' else 15
            threat_list = ', '.join(threats)
            score = self._add(findings, score, pts, '🚨🚨',
                f'KNOWN MALICIOUS SITE — {site_type.upper()}',
                f'This site is in our threat database as a known {"critical" if pts==20 else "high"}-risk '
                f'destination. Identified risks: {threat_list}. Do not visit this site under any '
                f'circumstances.')

        
        for pattern, explanation in self.scam_patterns:
            if re.search(pattern, domain, re.IGNORECASE):
                score = self._add(findings, score, 6, '🚨',
                    f'SCAM INDICATOR IN DOMAIN: "{pattern}"',
                    explanation)

       
        for kw, explanation in self.suspicious_keywords.items():
            if kw in domain_clean or kw in original_lower:
                score = self._add(findings, score, 3, '⚠️',
                    f'SUSPICIOUS KEYWORD: "{kw}"',
                    explanation)

    
        for brand, legit_domains in self.legitimate_brands.items():
            if brand in domain or brand in original_lower:
                is_legit = any(ld in domain for ld in legit_domains)
                if not is_legit:
                    score = self._add(findings, score, 8, '🚨',
                        f'BRAND IMPERSONATION: "{brand}"',
                        f'This URL contains the brand name "{brand}" but is NOT hosted on the '
                        f'real {brand} website (which would be {legit_domains[0]}). '
                        f'This is a fake/impersonation site designed to steal your '
                        f'{brand} credentials or payment details. Never log in here.')

      
        for term, explanation in self.piracy_indicators.items():
            if term in domain_clean or term in original_lower:
                score = self._add(findings, score, 5, '🏴‍☠️',
                    f'PIRACY INDICATOR: "{term}"',
                    explanation)

      
        for term in self.streaming_piracy_terms:
            if term in domain or term in original_lower:
                score = self._add(findings, score, 8, '🚨',
                    f'ILLEGAL STREAMING SITE: "{term}"',
                    f'This site is associated with illegal movie/TV/anime streaming. '
                    f'These sites violate copyright law and are well-known for serving '
                    f'malicious advertisements that can infect your device. Even just '
                    f'visiting them can trigger malware downloads.')

       
        tld = self.get_tld(domain)
        if tld in self.high_risk_tlds:
            score = self._add(findings, score, 4, '⚠️',
                f'HIGH-RISK TOP-LEVEL DOMAIN: "{tld}"',
                self.high_risk_tlds[tld])

      
        digits = sum(c.isdigit() for c in domain.split('.')[0])
        if digits >= 5:
            score = self._add(findings, score, 3, '⚠️',
                f'HEAVILY NUMERIC DOMAIN ({digits} digits)',
                'Domains with many numbers are often auto-generated by phishing kits or '
                'used to create disposable scam sites quickly. Legitimate businesses choose '
                'memorable names, not strings of numbers.')

        return score, findings

    
    def generate_report(self, original_input, total_score, all_findings, analysis_type):
        print(f"\n📊 SECURITY ANALYSIS REPORT")
        print("─" * 58)
        print(f"   Input:      {original_input}")
        print(f"   Analysis:   {analysis_type}")
        print(f"   Time:       {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        max_score = 100
        bar_filled  = min(int((total_score / max_score) * 20), 20)
        bar_empty   = 20 - bar_filled
        threat_bar  = '█' * bar_filled + '░' * bar_empty
        print(f"   Threat Score: {total_score}/{max_score}  [{threat_bar}]")
        print("─" * 58)

        if all_findings:
            print(f"\n🚨 {len(all_findings)} RED FLAG(S) DETECTED — Plain-English Breakdown:\n")
            for i, f in enumerate(all_findings, 1):
                print(f"  {f['emoji']} Flag #{i}: {f['title']}")
                
                words = f['explanation'].split()
                line  = "     ➜ "
                for w in words:
                    if len(line) + len(w) + 1 > 70:
                        print(line)
                        line = "       " + w + " "
                    else:
                        line += w + " "
                if line.strip():
                    print(line)
                print()
        else:
            print(f"\n✅ NO THREATS DETECTED")
            print("   This appears to be safe based on current analysis.")

        
        print(f"\n🎯 FINAL VERDICT:", end=" ")
        if total_score >= 25:
            print("💀 CRITICAL THREAT — EXTREME DANGER!")
            print("   🚫🚫🚫 DO NOT VISIT THIS SITE UNDER ANY CIRCUMSTANCES!")
            print("   🔥 This site is highly likely to steal your data,")
            print("      infect your device, or defraud you of money.")
            print("   📌 If you received this link in an email or message,")
            print("      report it as phishing and delete the message.")
        elif total_score >= 16:
            print("🚨 HIGH THREAT — VERY DANGEROUS!")
            print("   🚫🚫 AVOID COMPLETELY.")
            print("   ⚠️  Multiple serious red flags detected. This site is")
            print("      very likely malicious, illegal, or a phishing trap.")
        elif total_score >= 10:
            print("🟠 MEDIUM-HIGH THREAT — DO NOT PROCEED!")
            print("   🚫 Multiple concerning signals detected.")
            print("   🔍 This site has too many red flags to trust.")
            print("   💡 If you need this service, find it through an")
            print("      official source rather than this link.")
        elif total_score >= 5:
            print("🟡 MEDIUM RISK — Proceed with caution")
            print("   ⚠️  Some suspicious signals found.")
            print("   🔍 Do not enter passwords or payment info.")
            print("   💡 Verify this is the correct official website")
            print("      before doing anything on it.")
        elif total_score >= 2:
            print("🟢 LOW RISK — Minor concerns only")
            print("   👀 Generally looks safe, but stay alert.")
            print("   💡 Always verify you're on the real site")
            print("      before logging in or paying.")
        else:
            print("✅ CLEAN — No significant risks detected")
            print("   👍 This looks safe based on our analysis.")
            print("   💡 Remember: no tool is 100% perfect.")
            print("      Always stay alert online.")

        print("=" * 58)

    

    def analyze_input(self, user_input):
        print(f"\n🔍 Analyzing: '{user_input}'")
        print("─" * 60)

        normalized_url, malformed_flags = self.normalize_input(user_input)
        domain = self.extract_domain(normalized_url)

        is_bare_name = ('.' not in user_input and
                        not user_input.startswith(('http', 'https')))
        analysis_type = ("Website / Application Name Analysis" if is_bare_name
                         else "Full URL & Domain Analysis")

        all_findings = []
        total_score  = 0

        
        s_score, s_findings = self.analyze_structure(user_input, normalized_url,
                                                     domain, malformed_flags)
        total_score  += s_score
        all_findings += s_findings

      
        c_score, c_findings = self.analyze_domain_content(domain, user_input)
        total_score  += c_score
        all_findings += c_findings

      
        seen    = set()
        unique  = []
        for f in all_findings:
            if f['title'] not in seen:
                seen.add(f['title'])
                unique.append(f)
        all_findings = unique

        self.generate_report(user_input, total_score, all_findings, analysis_type)
        return total_score




def main():
    detector = AdvancedThreatDetector()
    detector.show_welcome()

    
    print("🚀 QUICK DEMO — Testing a mix of safe and dangerous inputs:\n")
    demos = [
        "http//scam-click.com",
        "paypal-verify-secure-login.xyz",
        "https://google.com",
        "soap2day.to",
        "free-crack-download.tk",
    ]
    for example in demos:
        detector.analyze_input(example)
        time.sleep(0.6)

    
    print("\n🎯 READY FOR YOUR INPUT!")
    print("Enter websites, app names, or full URLs to analyze.")
    print("Type 'help' for tips, or 'quit' to exit.")
    print("=" * 60)

    count = 0
    while True:
        try:
            print(f"\nAnalysis #{count + 1}")
            user_input = input("🎯 Enter website/URL to analyze: ").strip()

            if user_input.lower() in ('quit', 'exit', 'q'):
                print(f"\n📈 Session Summary: {count} items analyzed")
                print("Thank you for using the Advanced Threat Detector!")
                print("Stay safe online! 🔒")
                break
            elif user_input.lower() == 'help':
                print("\n💡 HELP — What you can analyze:")
                print("   • Full URLs:         https://example.com")
                print("   • Malformed URLs:    http//scam.com, hxxps://evil.com")
                print("   • Domain names:      google.com, evil-phish.xyz")
                print("   • Website names:     facebook, aniwatchtv, steamrip")
                print("   • App names:         whatsapp, spotify, cracked-photoshop")
                print("   Type 'quit' to exit.")
            elif not user_input:
                print("⚠️  Please enter something to analyze.")
            else:
                count += 1
                detector.analyze_input(user_input)
            print(f"\n{'=' * 60}")

        except KeyboardInterrupt:
            print(f"\n\n📊 Session completed! Analyzed {count} items.")
            print("Thank you for protecting your digital security! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with a different input.")

if __name__ == "__main__":
    main()
