# SecureVault — Automated Credential Rotation & Encryption System

> Securely rotate credentials, encrypt sensitive data, and automate secret management.

## Overview

**SecureVault** is a Python-based security desktop application built to automate password rotation and encrypted credential storage. It securely generates strong passwords, encrypts vault data, schedules periodic updates, and notifies users via email whenever credentials change.

The system is designed for secure local credential management without requiring any cloud services.

---

## Features

### Automated Password Rotation

* Generates strong **20-character passwords**
* Randomized letters, digits, and special symbols
* Scheduled credential updates

### Data Encryption

* Uses **Fernet symmetric encryption**
* Encrypts sensitive credentials into `vault.enc`
* Secure local storage

### Email Notifications

* Sends updated credentials via Gmail SMTP
* Configurable expiration time
* Secure password delivery workflow

### GUI Interface

* Built using **CustomTkinter**
* Dark themed desktop UI
* Live status display
* Real-time logs

### Scheduler

* Automatic timed rotation
* Background execution
* Configurable intervals

---

## Tech Stack

| Component  | Technology            |
| ---------- | --------------------- |
| Language   | Python                |
| GUI        | CustomTkinter         |
| Encryption | cryptography (Fernet) |
| Scheduling | schedule              |
| Email      | smtplib               |
| OS         | Windows               |

---

## Project Structure

```text
SecureVault/
├── vault.py
├── gui.py
├── launch.bat
├── vault.enc
├── key.key
└── requirements.txt
```

---

## Core Modules

### vault.py

Backend security engine.

Functions:

* `generate_password()` → Creates secure random credentials
* `save_key()` → Generates encryption key
* `encrypt_vault()` → Encrypts vault data
* `send_email()` → Sends credentials securely
* `rotate_password()` → Handles automated rotation

---

### gui.py

Frontend application.

Features:

* Dark mode UI
* 600 × 450 fixed window
* Status panel
* Live logs
* Manual trigger support

---

### launch.bat

Startup launcher.

* Activates virtual environment
* Runs GUI automatically
* Simplified startup process

---

## Workflow

```text
Password Rotation Trigger
        ↓
Generate New Password
        ↓
Encrypt Vault Data
        ↓
Store Securely
        ↓
Send Email Notification
        ↓
Log Event
```

---

## Security Design

* Local-only encrypted storage
* Automatic key management
* No plaintext vault files
* No cloud dependency
* Scheduled secret refresh
* Encrypted backup

---

## Future Scope

* Multi-user credential vault
* Web dashboard
* OTP integration
* Audit trail
* Role-based access
* Mobile app support

---

## Author

**Samrudh**

Tech Enthusiast

Computer Science & Technology Student | Innovator

---

## License

Private Project

