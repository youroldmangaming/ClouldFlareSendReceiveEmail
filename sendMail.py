import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Load .env file
load_dotenv()

# Email configuration
smtp_host = os.getenv("SMTP_HOST")
smtp_port = os.getenv("SMTP_PORT")
smtp_user = os.getenv("SMTP_USER")  # Your Gmail address
smtp_password = os.getenv("SMTP_PASSWORD")  # Your Gmail App Password
from_email = "admin@youroldmangaming.com"
to_email = "wilsomrm2@yahoo.com" # Or any email you want to test with

def send_test_email():
    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f'Test Email from Python - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    body = """
    This is a test email sent from Python using Gmail SMTP.
    If you receive this, your SMTP configuration is working correctly.
    
    Configuration used:
    SMTP Host: {host}
    SMTP Port: {port}
    From: {from_email}
    Auth User: {user}
    """.format(
        host=smtp_host,
        port=smtp_port,
        from_email=from_email,
        user=smtp_user
    )
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session
        print(f"Connecting to {smtp_host}:{smtp_port}...")
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        
        # Login
        print(f"Attempting to login with user: {smtp_user}")
        server.login(smtp_user, smtp_password)
        
        # Send email
        print(f"Sending email from {from_email} to {to_email}...")
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
    finally:
        if 'server' in locals():
            server.quit()

if __name__ == "__main__":
    if not smtp_user or not smtp_password:
        print("Error: SMTP_USER and SMTP_PASSWORD not found in .env file")
    else:
        send_test_email()






