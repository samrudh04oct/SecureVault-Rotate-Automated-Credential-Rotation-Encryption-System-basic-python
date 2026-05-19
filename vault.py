import os
import time
import schedule
import secrets
import string
import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")
OWNER_EMAIL = os.getenv("OWNER_EMAIL")

VAULT_FILE = "vault.enc"
KEY_FILE = "vault.key"

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(20))

def save_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def encrypt_vault():
    key = save_key()
    f = Fernet(key)
    data = b"My super secret vault data"
    encrypted = f.encrypt(data)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

def send_email(password):
    msg = MIMEText(f"Vault password updated:\n\n{password}\n\nValid for 4 hours.")
    msg["Subject"] = "Vault Password Update"
    msg["From"] = EMAIL
    msg["To"] = OWNER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, EMAIL_PASS)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        print("\n[!] Authentication Failed!")
        print("    If you are using Gmail, you likely need an 'App Password'.")
        print("    1. Enable 2-Step Verification in Google Account Settings.")
        print("    2. Go to 'App passwords' (search in settings).")
        print("    3. Generate a new password and use it in your .env file as EMAIL_PASS.")
    except Exception as e:
        print(f"\n[!] Failed to send email: {e}")

def rotate_password():
    password = generate_password()
    encrypt_vault()
    send_email(password)
    print("Password rotated.")

def start_scheduler():
    print("Scheduler started. Running loop...")
    rotate_password()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_scheduler()
