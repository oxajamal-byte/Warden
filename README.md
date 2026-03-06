# Warden

A phishing detetcion tool that analyzes URLs and application names and returns a danger score from 1 to 10 with a plain English explanation of what could go wrong. 

## The Problem 

Phishing is one of the most common cyberattacks on the internet today. Attackers trick people into clicking malicious links or entering sensitive information by pretending to be trusted companies, services, or individuals. 

These attacks lead to stolen passwords, financial loss, compromised accounts, and sometimes even full network breaches. What makes phishing especially dangerous is that it targets everyday users who may not have the technical knowledge to recognize suspicious messages or websites.

This project was created to help detect and identify potential phishing attempts by analyzing links and suspicious indicators. The goal is to provide a simple tool that helps users recognize threats before they click something that could compromise their security.

## What It Does 

- You enter a URL or app name
- Warden returns a score from 1 (safe) to 10 (crtitical risk)
- Plain English explanation of every red flag detected

  ## How It Works

The tool analyzes URLs and domain names to identify phishing, scams, and malicious websites. It uses rules and patterns to generate a threat score, helping users identify suspecious links before interacting with them. 

-Matches the domain against a database of common high risk sites, immediately flagging phishing, scams, or privacy.

looks for words like login, verify, secure, account, and update. Suspecious keywords that are commonly used to trick users. 

Checks if a domain mimics a popular brand like PayPal, Google, Microsoft, etc. but not hosted on the legitmate domain. 

Flags common domains with extensions abused in phishing campaigns, .tk, .ml, .xyz, .top.

Flags domains that distrabutes pirated content or software, which often include malware or malicious ads. 

## Risk Scoring

Each red flag adds points to a threat score which classifies the domain as 

Low Risk = Likely Safe 

Medium Risk = Suspecious, proceed with caution 

High Risk = Very dangerous, avoid it 

Criticial = Likely malicious do not visit 

## How To Run It 

| KALI |

git clone https://github.com/oxajamal-byte/Warden-.git

cd Warden-

pip install -r requirements.txt

python3 main.py

| MacOS |

git clone https://github.com/oxajamal-byte/Warden-.git

cd Warden-

pip3 install -r requirements.txt

python3 main.py

| Windows |

git clone https://github.com/oxajamal-byte/Warden-.git

cd Warden-

pip install -r requirements.txt

python main.py

## What's Coming Next 
-Browser extension version 

-API endpoint for developers to integrate 

-Machine learning scoring model 

## Built By 

Jamal 16 year old cybersecurity enthusiast. Built this at 15 because I wanted non technical people to have a way to check suspecious links before clicking them. 


