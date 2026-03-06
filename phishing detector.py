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
        # Known malicious/piracy sites database
        self.known_malicious_sites = {
            'aniwatchtv.to': {
                'risk': 'HIGH',
                'type': 'Piracy Streaming',
                'threats': ['Copyright infringement', 'Malware risk', 'Unverified ads']
            },
            'movies2watch.tv': {
                'risk': 'HIGH', 
                'type': 'Piracy Streaming',
                'threats': ['Illegal content', 'Malware distribution', 'Phishing ads']
            },
            'fmoviesz.to': {
                'risk': 'HIGH',
                'type': 'Piracy Streaming', 
                'threats': ['Copyright violation', 'Security risks', 'Malicious ads']
            },
            'soap2day.to': {
                'risk': 'CRITICAL',
                'type': 'Piracy Streaming',
                'threats': ['Malware hosting', 'Illegal streaming', 'Data theft risk']
            },
            '123movies': {
                'risk': 'HIGH',
                'type': 'Piracy Streaming',
                'threats': ['Copyright infringement', 'Malware', 'Phishing']
            }
        }
        
        self.suspicious_keywords = [
            'login', 'verify', 'secure', 'account', 'update', 'banking', 
            'password', 'signin', 'validation', 'authenticate', 'confirm',
            'security', 'verification', 'credential', 'profile', 'wallet',
            'payment', 'billing', 'invoice', 'statement', 'recover',
            'unlock', 'suspend', 'limited', 'actionrequired'
        ]
        
        self.piracy_indicators = [
            'rip', 'crack', 'keygen', 'torrent', 'pirate', 'freedownload',
            'serial', 'patch', 'warez', 'cracked', 'fullversion', 'nosteam',
            'repack', 'codex', 'fitgirl', 'igg', 'skidrow', 'plaza', 'reloaded',
            'watchfree', 'freemovies', 'streamfree', 'putlocker', 'movie4k'
        ]
        
        self.streaming_piracy_terms = [
            'aniwatch', 'movies2watch', 'fmovies', 'soap2day', '123movies',
            'putlocker', 'solarmovie', 'yts', 'eztv', 'rarbg', 'limetorrents',
            'kickasstorrents', 'piratebay', '1337x', 'torlock'
        ]
        
        self.malware_indicators = [
            'free', 'download', 'installer', 'setup', 'crack', 'keygen',
            'patch', 'activator', 'generator', 'hack', 'cheat', 'mod'
        ]
        
        self.high_risk_tlds = ['.to', '.ru', '.cn', '.cc', '.tk', '.ml', '.ga', '.cf', '.xyz', '.top', '.club', '.info', '.biz', '.online']

        self.legitimate_brands = {
            'paypal': ['paypal.com', 'paypal-business.com'],
            'microsoft': ['microsoft.com', 'live.com', 'outlook.com'],
            'google': ['google.com', 'gmail.com', 'youtube.com'],
            'apple': ['apple.com', 'icloud.com'],
            'amazon': ['amazon.com', 'aws.amazon.com'],
            'facebook': ['facebook.com', 'fb.com'],
            'netflix': ['netflix.com'],
            'steam': ['steam.com', 'steampowered.com'],
            'deepseek': ['deepseek.com'],
            'github': ['github.com'],
            'twitter': ['twitter.com', 'x.com'],
            'instagram': ['instagram.com'],
            'disney': ['disneyplus.com'],
            'hbo': ['hbomax.com'],
            'hulu': ['hulu.com'],
            'crunchyroll': ['crunchyroll.com']
        }

    def show_welcome(self):
        """Display welcome message and features"""
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
        print("   • Full URLs (https://example.com)")
        print("   • Website names (google, facebook, steamrip)")
        print("   • Application names (whatsapp, spotify, photoshop)")
        print("   • Suspicious links from emails or messages")
        
        print("\n🔍 I DETECT:")
        print("   ✅ Phishing attempts")
        print("   ✅ Brand impersonation") 
        print("   ✅ Piracy/copyright sites")
        print("   ✅ Malware distribution")
        print("   ✅ Illegal streaming sites")
        print("   ✅ Known malicious websites")
        
        print("\n💡 TIP: You can enter just a name like 'paypal' or full URL!")
        print("⭐" * 35)
        
        # Show a cool loading animation
        print("\nInitializing detection systems", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(" ✅ READY!\n")

    def normalize_input(self, user_input):
        """Convert any input (name, URL, app name) into a standardized format"""
        user_input = user_input.strip().lower()
        
        # If it's already a full URL, return as is
        if user_input.startswith(('http://', 'https://')):
            return user_input
        
        # If it contains a dot, treat as domain
        if '.' in user_input and not any(char in user_input for char in [' ', '\t']):
            if not user_input.startswith(('http://', 'https://')):
                return 'https://' + user_input
        
        # Otherwise, treat as website/application name and create test domain
        return 'https://' + user_input + '-test-security-check.com'

    def extract_domain(self, url):
        """Extract domain from URL"""
        try:
            if '://' in url:
                url = url.split('://', 1)[1]
            domain = url.split('/')[0]
            domain = domain.split(':')[0]
            return domain.lower()
        except:
            return url.lower()

    def check_known_malicious(self, domain):
        """Check against database of known malicious sites"""
        for known_site, info in self.known_malicious_sites.items():
            if known_site in domain:
                return info['risk'], info['type'], info['threats']
        return None, None, None

    def analyze_website_name(self, original_input, domain):
        """Special analysis for website/application names"""
        risk_factors = []
        score = 0
        
        original_lower = original_input.lower()
        
        # Check if it's in known malicious database
        risk_level, site_type, threats = self.check_known_malicious(original_lower)
        if risk_level:
            if risk_level == 'CRITICAL':
                score += 15
                risk_factors.append(f"🚨 KNOWN MALICIOUS SITE: {site_type}")
                for threat in threats:
                    risk_factors.append(f"   🚫 {threat}")
            else:
                score += 10
                risk_factors.append(f"🚨 KNOWN HIGH-RISK SITE: {site_type}")
                for threat in threats:
                    risk_factors.append(f"   ⚠️  {threat}")
        
        # Check for streaming piracy terms
        for piracy_term in self.streaming_piracy_terms:
            if piracy_term in original_lower:
                score += 8
                risk_factors.append(f"🚨 ILLEGAL STREAMING: '{piracy_term}' detected")
                risk_factors.append("   ⚠️  Copyright infringement violation")
                risk_factors.append("   🦠 High malware risk from unverified ads")
                risk_factors.append("   👮 Legal consequences possible")
        
        # Check if it's a known legitimate brand
        is_known_brand = any(brand in original_lower for brand in self.legitimate_brands.keys())
        
        # Check for suspicious modifications to known brands
        for brand in self.legitimate_brands.keys():
            if brand in original_lower:
                # Check for typos or modifications
                if original_lower != brand and not any(legit in original_lower for legit in self.legitimate_brands[brand]):
                    score += 2
                    risk_factors.append(f"Modified brand name: {brand}")
        
        # Check for piracy indicators in the name
        for indicator in self.piracy_indicators:
            if indicator in original_lower:
                score += 5
                risk_factors.append(f"🚨 PIRACY INDICATOR: '{indicator}'")
                risk_factors.append("   ⚠️  May distribute illegal/copyrighted content")
        
        # Check for malware-related terms
        for indicator in self.malware_indicators:
            if indicator in original_lower and not is_known_brand:
                score += 4
                risk_factors.append(f"🦠 MALWARE INDICATOR: '{indicator}'")
                risk_factors.append("   ⚠️  May contain viruses or malicious software")
        
        # Very short or very long names
        if len(original_input) < 4:
            score += 1
            risk_factors.append("Very short name (could be fake)")
        elif len(original_input) > 30:
            score += 1
            risk_factors.append("Unusually long name")
        
        return score, risk_factors

    def analyze_url_structure(self, url, domain):
        """Analyze URL structure for threats"""
        risk_factors = []
        score = 0
        
        # Check known malicious sites database
        risk_level, site_type, threats = self.check_known_malicious(domain)
        if risk_level:
            if risk_level == 'CRITICAL':
                score += 20
                risk_factors.append(f"🚨🚨 KNOWN MALICIOUS WEBSITE: {site_type}")
                for threat in threats:
                    risk_factors.append(f"   🚫 {threat}")
                risk_factors.append("   🔥 EXTREME DANGER - DO NOT VISIT!")
            else:
                score += 15
                risk_factors.append(f"🚨 KNOWN HIGH-RISK WEBSITE: {site_type}")
                for threat in threats:
                    risk_factors.append(f"   ⚠️  {threat}")
                risk_factors.append("   🚫 HIGH RISK - Avoid completely!")
        
        # Check for streaming piracy in domain
        for piracy_term in self.streaming_piracy_terms:
            if piracy_term in domain:
                score += 10
                risk_factors.append(f"🚨 ILLEGAL STREAMING SITE: '{piracy_term}'")
                risk_factors.append("   ⚠️  Copyright violation - illegal content")
                risk_factors.append("   🦠 High malware risk from malicious ads")
                risk_factors.append("   💀 Legal consequences possible")
        
        # High-risk TLD detection
        tld = '.' + domain.split('.')[-1] if '.' in domain else ''
        if tld in self.high_risk_tlds:
            score += 4
            risk_factors.append(f"🚨 HIGH-RISK DOMAIN: {tld} extension")
            risk_factors.append("   ⚠️  Commonly used for malicious sites")
        
        # IP address detection
        ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        clean_domain = domain.replace('https://', '').replace('http://', '')
        if re.match(ip_pattern, clean_domain):
            score += 5
            risk_factors.append("🚨 USES IP ADDRESS DIRECTLY")
            risk_factors.append("   ⚠️  Highly suspicious - common in malware")
        
        # @ symbol obfuscation
        if '@' in url:
            score += 5
            risk_factors.append("🚨 USES @ SYMBOL TO HIDE REAL DOMAIN")
            risk_factors.append("   ⚠️  Common phishing technique")
        
        # Excessive hyphens
        if domain.count('-') > 3:
            score += 3
            risk_factors.append("Excessive hyphens in domain")
        
        # Suspicious keywords
        for keyword in self.suspicious_keywords:
            if keyword in domain:
                score += 2
                risk_factors.append(f"Suspicious keyword: '{keyword}'")
        
        # Brand impersonation
        for brand, legitimate_domains in self.legitimate_brands.items():
            if brand in domain:
                is_legitimate = any(legit_domain in domain for legit_domain in legitimate_domains)
                if not is_legitimate:
                    score += 5
                    risk_factors.append(f"🚨 BRAND IMPERSONATION: {brand}")
                    risk_factors.append("   ⚠️  Likely phishing for credentials")
        
        return score, risk_factors

    def generate_report(self, original_input, total_score, risk_factors, analysis_type):
        """Generate comprehensive security report"""
        print(f"\n📊 SECURITY ANALYSIS REPORT")
        print("─" * 50)
        print(f"   Input: {original_input}")
        print(f"   Analysis: {analysis_type}")
        print(f"   Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Threat Score: {total_score}/35")
        
        if risk_factors:
            print(f"\n🚨 THREATS DETECTED:")
            for i, factor in enumerate(risk_factors, 1):
                print(f"   {i:2d}. {factor}")
        else:
            print(f"\n✅ NO THREATS DETECTED")
            print("   This appears to be safe based on current analysis")
        
        # Final verdict with enhanced danger levels
        print(f"\n🎯 FINAL VERDICT:", end=" ")
        if total_score >= 20:
            print("💀 CRITICAL THREAT - EXTREME DANGER!")
            print("   🚫🚫🚫 DO NOT VISIT - KNOWN MALICIOUS WEBSITE!")
            print("   🔥 Contains malware, illegal content, or phishing!")
        elif total_score >= 15:
            print("🚨🚨 HIGH THREAT - VERY DANGEROUS!")
            print("   🚫🚫 AVOID COMPLETELY - Known high-risk site!")
            print("   ⚠️  Likely contains illegal content or malware!")
        elif total_score >= 10:
            print("🚨 MEDIUM-HIGH THREAT - DANGEROUS!")
            print("   🚫 Do not visit - Multiple high-risk factors!")
            print("   🦠 Potential malware or legal issues!")
        elif total_score >= 5:
            print("🟡 MEDIUM RISK - Multiple concerns")
            print("   🔍 Proceed with extreme caution")
        elif total_score >= 2:
            print("🟡 LOW RISK - Minor concerns")
            print("   👀 Generally safe but stay alert")
        else:
            print("✅ CLEAN - No significant risks")
            print("   👍 Very low threat level")

    def analyze_input(self, user_input):
        """Main analysis function for any type of input"""
        print(f"\n🔍 Analyzing: '{user_input}'")
        print("─" * 60)
        
        # Normalize the input
        normalized_url = self.normalize_input(user_input)
        domain = self.extract_domain(normalized_url)
        
        total_score = 0
        all_risk_factors = []
        analysis_type = "Full URL Analysis" if '.' in user_input and not user_input.startswith(('http://', 'https://')) else "Name/Application Analysis"
        
        # Analyze based on input type
        if not user_input.startswith(('http://', 'https://')) and '.' not in user_input:
            analysis_type = "Website/Application Name Analysis"
            name_score, name_risks = self.analyze_website_name(user_input, domain)
            total_score += name_score
            all_risk_factors.extend(name_risks)
        
        # Always analyze URL structure
        url_score, url_risks = self.analyze_url_structure(normalized_url, domain)
        total_score += url_score
        all_risk_factors.extend(url_risks)
        
        # Generate the report
        self.generate_report(user_input, total_score, all_risk_factors, analysis_type)
        
        return total_score

def main():
    detector = AdvancedThreatDetector()
    
    # Show awesome welcome screen
    detector.show_welcome()
    
    # Demo with known dangerous sites
    print("🚀 QUICK DEMO - Testing known dangerous sites:")
    dangerous_demos = [
        "aniwatchtv.to",
        "movies2watch.tv", 
        "https://google.com",
        "fmoviesz.to",
        "paypal-verify-login.com"
    ]
    
    for example in dangerous_demos:
        detector.analyze_input(example)
        print("\n" + "=" * 60)
        time.sleep(1)
    
    # Interactive mode
    print("\n🎯 READY FOR YOUR INPUT!")
    print("Enter websites, app names, or full URLs to analyze")
    print("Type 'help' for options, 'quit' to exit")
    print("=" * 60)
    
    analysis_count = 0
    
    while True:
        try:
            print(f"\nAnalysis #{analysis_count + 1}")
            user_input = input("🎯 Enter website/URL to analyze: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"\n📈 Session Summary: {analysis_count} items analyzed")
                print("Thank you for using the Advanced Threat Detector!")
                print("Stay safe online! 🔒")
                break
            
            elif user_input.lower() == 'help':
                print("\n💡 HELP - What you can analyze:")
                print("   • Full URLs: https://example.com")
                print("   • Domain names: google.com") 
                print("   • Website names: facebook, aniwatchtv")
                print("   • App names: whatsapp, spotify")
                print("   • Suspicious names: freecracks, movies2watch")
                print("   • Type 'quit' to exit")
                continue
            
            elif not user_input:
                print("⚠️  Please enter something to analyze")
                continue
            
            analysis_count += 1
            detector.analyze_input(user_input)
            
            print(f"\n{'='*60}")
            
        except KeyboardInterrupt:
            print(f"\n\n📊 Session completed! Analyzed {analysis_count} items")
            print("Thank you for protecting your digital security! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with a different input")

if __name__ == "__main__":
    main()