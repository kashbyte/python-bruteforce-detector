## 🛡️ Python Brute Force Detection & Alerting System

A Python based security monitoring tool that detects SSH brute force login attempts by parsing authentication logs, applying time window analysis, blocking malicious IP addresses, logging security events, and sending real time Telegram alerts.

This project simulates a simplified Security Operations Center (SOC) detection and alerting workflow and is designed as a portfolio project for cybersecurity university applications.

## 📌 Features

Time based brute force attack detection

SSH authentication log parsing

Persistent IP blocklist to prevent repeated attacks

Structured security logging with severity levels

Real time Telegram alerting

Secure secret management using .env files

Cross platform development (tested on Windows)

## 🧠 How It Works

Reads SSH authentication logs from sample_auth.log

Tracks failed login attempts per IP address

Detects multiple failures within a defined time window

Flags the source IP as a brute force attacker

Logs the security incident

Sends a Telegram alert

Adds the IP address to a persistent blocklist

## 📥 How to Pull the Project

Clone the repository from GitHub:

```bash
git clone https://github.com/kashbyte/python-bruteforce-detector.git
```
Navigate into the project directory:
```text
cd python-bruteforce-detector
```
## 📸 Screenshots

### Automated IP Blocking Output
Shows the blocked IPs.
<img width="985" height="111" alt="image" src="https://github.com/user-attachments/assets/f49f7825-2fad-476d-b70d-ff27b9d8203e" />


---

### Telegram Alert Notification
Real time alert sent to Telegram when a brute force attack is detected.
<img width="978" height="400" alt="image" src="https://github.com/user-attachments/assets/19d6c459-bb14-45df-b230-b2e8e5f5acee" />

---

### Security Log File
<img width="978" height="295" alt="image" src="https://github.com/user-attachments/assets/1bb72f92-8fd3-436b-b544-1e6103e30eb1" />


---
## 📁 Project Structure

```text
python-bruteforce-detector/
├── detector.py            # Main brute force detection script
├── sample_auth.log        # Sample SSH authentication log (provided for testing)
├── blocked_ips.txt        # Persistent blocklist (auto-generated, gitignored)
├── security.log           # Security event logs (auto-generated, gitignored)
├── .env                   # Environment variables (gitignored)
├── .gitignore
└── README.md
```
## ⚙️ Requirements

* Python 3.9 or higher
* pip
* Telegram account
* Python Dependencies

```text
python -m pip install requests python-dotenv
```

## 🔐 Secure Configuration (Important)

Secrets are never stored in the source code.

1. Create a .env file

Create a file named .env in the project root:
```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```
2. Git Safety

The .env file is excluded from version control using .gitignore to prevent credential leakage.

## 🧪 Testing With Sample Logs

This repository includes a sample SSH authentication log file named sample_auth.log.

Users can:

* Modify the file
* Add more failed login entries
* Simulate brute force attacks
* Observe detection, logging, blocking, and alerting behavior
* No live server is required for testing.

## 🚀 How to Run
1. Ensure sample_auth.log exists in the project directory
2. Configure your .env file
3. Run the detector:
```text
python detector.py
```
## 📄 Example Security Log Output
```text
2025-12-26 22:53:05 | WARNING | 🚨 Brute Force Alert
IP: 192.168.1.10
Attempts: 3
Time window: 60 seconds
```

## 📲 Example Telegram Alert
```text
🚨 Brute Force Alert
IP: 192.168.1.10
Attempts: 3
Time window: 60 seconds
```
## 🛡️ Security Practices Implemented

* Environment variable based secret management
* No hardcoded credentials
* Persistent attack state handling
* Structured logging with timestamps and severity
* Graceful failure handling

## 📈 Future Enhancements
* Email alerting support
* Configuration file support (YAML or JSON)
* Firewall or iptables integration
* Unit testing for detection logic
* Docker containerization

## 🎯 Purpose of This Project

This project demonstrates:
* Log analysis skills
* Defensive security mindset
* Alerting pipeline design
* Secure coding practices
* SOC style detection logic
