from collections import defaultdict
from datetime import datetime
import logging
import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "sample_auth.log")
BLOCKLIST_FILE = os.path.join(BASE_DIR, "blocked_ips.txt")
SECURITY_LOG = os.path.join(BASE_DIR, "security.log")

# Logging configuration
logging.basicConfig(
    filename=SECURITY_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logging.info("Brute force detection script started")

# Load blocked IPs
def load_blocked_ips():
    try:
        with open(BLOCKLIST_FILE, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

# Block IP function
def block_ip(ip):
    blocked_ips = load_blocked_ips()

    if ip in blocked_ips:
        logging.info(f"IP {ip} already blocked")
        return False

    with open(BLOCKLIST_FILE, "a") as file:
        file.write(ip + "\n")

    logging.warning(f"IP {ip} added to blocklist")
    return True

# Telegram alert function
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{os.getenv("TELEGRAM_BOT_TOKEN")}/sendMessage"
    payload = {
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
        "text": message
    }

    try:
        requests.post(url, data=payload, timeout=5)
        logging.info("Telegram alert sent successfully")
    except Exception as e:
        logging.error(f"Failed to send Telegram alert: {e}")

# Brute force detection logic
failed_attempts = defaultdict(list)

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            timestamp_str = " ".join(parts[0:3])
            timestamp = datetime.strptime(
                "2025 " + timestamp_str, "%Y %b %d %H:%M:%S"
            )

            ip_address = parts[parts.index("from") + 1]
            failed_attempts[ip_address].append(timestamp)

TIME_WINDOW = 60
ATTEMPT_THRESHOLD = 3

for ip, timestamps in failed_attempts.items():
    timestamps.sort()

    for i in range(len(timestamps)):
        window_start = timestamps[i]
        window_end = window_start.timestamp() + TIME_WINDOW

        count = 1
        for j in range(i + 1, len(timestamps)):
            if timestamps[j].timestamp() <= window_end:
                count += 1

        if count >= ATTEMPT_THRESHOLD:
            alert_message = (
                f"🚨 Brute Force Alert\n"
                f"IP: {ip}\n"
                f"Attempts: {count}\n"
                f"Time window: {TIME_WINDOW} seconds"
            )

            logging.warning(alert_message)
            send_telegram_alert(alert_message)
            block_ip(ip)
            break

logging.info("Brute force detection script finished")
