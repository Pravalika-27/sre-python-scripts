import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your@email.com"
    msg["To"] = "to@email.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your@email.com", "password")
        server.send_message(msg)

send_alert("Alert: High CPU", "CPU usage has crossed 90%")