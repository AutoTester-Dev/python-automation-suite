# Automated Report Mailer

A Python automation tool designed to securely send generated reports (Excel/CSV) via email using Gmail's SMTP server.

## 🚀 Overview
This script streamlines the reporting process by automatically attaching a specified file and sending it to a designated recipient. It is built to be easily integrated into larger automation pipelines (e.g., sending daily weather or data reports).

## ⚠️ Security First: Important Configuration
**Security Warning:** Never hardcode your email credentials directly into the script. 

To use this script securely:
1. **Gmail App Password:** You must use an **App Password** for your Gmail account, not your regular login password. Go to your Google Account settings -> Security -> 2-Step Verification -> App passwords to generate one.
2. **Environment Variables:** Use a `.env` file to store your credentials safely:
   ```text
   SENDER_EMAIL=your_email@gmail.com
   APP_PASSWORD=your_16_digit_app_password
   RECEIVER_EMAIL=recipient@example.com
