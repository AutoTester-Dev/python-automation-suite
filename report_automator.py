import smtplib
import os
from email.message import EmailMessage

def send_report_email(file_path):
    # Check if the file exists in the directory
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found!")
        return

    # Configuration (Replace with your actual email details)
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient@example.com"
    password = "your_app_password"  # Use your 16-character App Password

    msg = EmailMessage()
    msg['Subject'] = "Automated Daily Weather Report"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content("Dear user, please find the attached daily weather report.")

    # Attach the Excel file
    with open(file_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', 
                           subtype='xlsx', filename=file_path)

    # Sending the email via Gmail SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        print(f"✅ Report '{file_path}' was sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    # Pointing to the file that already exists in your storage
    target_file = "Tashkent_Weather_Report.xlsx"
    send_report_email(target_file)
